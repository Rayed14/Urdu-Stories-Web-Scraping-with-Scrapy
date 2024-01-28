# Urdu-Stories-Web-Scraping-with-Scrapy
## Overview
This repository contains a Scrapy spider designed to scrape Urdu stories from the website UrduZone. The spider extracts text content, removes HTML tags, and filters out non-Urdu words and numbers. The collected Urdu stories are stored in a CSV file within the Scrapy project directory.

## Repository Structure
.
├── urdu_stories             # Scrapy project directory  
│   ├── scrapy.cfg  
│   └── urdu_stories         # Scrapy spider code  
│       ├── __init__.py  
│       ├── items.py         # Scrapy item definitions  
│       ├── middlewares.py   # Scrapy middlewares (if any)  
│       ├── pipelines.py     # Scrapy pipelines for data storage  
│       ├── settings.py      # Scrapy project settings  
│       └── spiders  
│           ├── __init__.py  
│           └── i20XXXX_urdu_stories_spider.py   # Scrapy spider for Urdu stories  
├── data                      # Folder containing CSV file with cleaned data  
│   └── urdu_stories.csv  
├── LaTeX_Report              # LaTeX report for documentation  
│   ├── main.tex  
│   └── references.bib  
├── README.md                 # Project README file  
└── requirements.txt          # Python dependencies  

## Getting Started
* Clone the Repository:

git clone https://github.com/your-username/urdu-stories-scrapy.git
## Install Dependencies:

pip install -r requirements.txt
* Run the Scrapy Spider:

cd urdu_stories
scrapy crawl i20XXXX_urdu_stories_spider
## How to Use
The Scrapy spider will start crawling the UrduZone website, extracting Urdu stories, and cleaning the data.

The cleaned Urdu stories will be stored in the data folder in a CSV file named urdu_stories.csv.

## Documentation
### Approach:

The Scrapy spider is configured to start from the UrduZone website.
It uses Scrapy selectors to extract text content from the website.
The spider implements a mechanism to remove HTML tags and filter out non-Urdu words and numbers.
### Challenges:

Document any challenges faced during the implementation.
### Code Comments:

The spider's code includes comments to explain the logic and important steps.
### LaTeX Report:

Refer to the LaTeX report in the LaTeX_Report folder for a detailed explanation of the project, approach, and challenges.
