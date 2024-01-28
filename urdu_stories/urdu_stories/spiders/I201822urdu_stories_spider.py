# Rayed Muhammad Saeed
# 20i-1822
# NLP Assignment 2
# i201822@nu.edu.pk

#importing the necassary libraries
import re
import scrapy 
from scrapy.selector import Selector
import csv

# Global list to store unique story links
uniqueLinks = []

# Defining the Spider class
class I201822Spider(scrapy.Spider):
    name = "I201822urdu_stories_spider"  #naming the spider
    allowed_domains = ["www.urduzone.net"]  #allowed domains for the spider to visit
    start_urls = ["https://www.urduzone.net/"] # Starting URL for scraping

    # POST request to make an empty search
    def start_requests(self):
        search_url = 'https://www.urduzone.net/'
        data = {
            's': '',  # Empty search query
            'submit': 'Search',
        }
        yield scrapy.FormRequest(search_url, formdata=data, callback=self.Searchparse)

    #parsing the search page stories and crawling through the pages
    def Searchparse(self, response):
        allLinks = []
        nextPageLink = "https://www.urduzone.net/page/" 
        for i in range(1, 226): #loop to go till the total number of pages that are there for the stories
            baseUrl = nextPageLink + str(i) + "/?s"
            allLinks.append(baseUrl)
            
        #going to the links that were extracted
        for link in allLinks:
            yield scrapy.Request(link, callback=self.parseSearchPage)
        
    # function to get the unique links of the search page    
    def parseSearchPage (self,response):
        links = response.css('h3.entry-title.td-module-title a::attr(href)').extract()
        allLinks = []
        for link in links:
            if link not in uniqueLinks:
                uniqueLinks.append(link) #storing the unique links from all the pages and all the links of stories on those pages
                allLinks.append(link)
                
        print("unique links: ", len(uniqueLinks))
        
        for link in allLinks:
            yield scrapy.Request(link, callback=self.parsestories)
    
    # parsing the stories on the links that were crawled
    def parsestories(self, response):
        nodes = response.css('div.tdb-block-inner.td-fix-index p::text')
        story = ''.join(nodes.extract())

        title = response.css('h1.tdb-title-text::text').get()
        cleanStories = self.cleanStory(story) #getting clean stories in this variable

        # if we get clean story as true then writing them into the csv file
        if cleanStories:
            with open('stories.csv', 'a', newline='', encoding='utf-8') as csvfile:
                Obj = csv.writer(csvfile)
                Obj.writerow([title, cleanStories.strip()])
        
    # cleaning the stories to ensure that there are no numbers or non urdu characters
    def cleanStory(self,story):
        # cleaned_text = re.sub(r'[^؀-ۿ ]', extractedStory)
        cleaned_text = re.findall(r'[\u0600-\u06FF]+', story)
        cleaned = ' '.join(cleaned_text)
        return cleaned