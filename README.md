# GodcheckerScrapper
A simple web scrapper to scrape [Godchecker](https://www.godchecker.com/) implemented using Scrapy and stored in SQLite3 database.

## Introduction

The scenario is as follows: You have been tasked by a historian to deep dive into the data. The goal here is to write a book on Religions and Mythology through time, so he is looking to use the data you have prepared (possibly in a SQL-like database for easy access!). The additional analysis on said dataset would also help kickstart the analysis that that would then be done by the data scientist.

There are three main objectives:
1. Your first objective is to scrape all facts and figures of every god from every pantheon
listed on the website. This should be completed in Python/Bash, using any additional
libraries when necessary.
2. Next, store the data in a way you think best fits a data processing/management scenario. Detail your decisions and choices in the README
3. From the data obtained, provide some interesting statistics and insights that you find relevant, interesting, or just fun.

## Architecture and Workflow
I chose [Scrapy](https://scrapy.org/) as one of the possible web scrapper frameworks for python, another well-known framework is [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). Scrapy would perform the scrapping workload to find all facts and figures of every god from every pantheon under the website. Afterwards, the data would be stored in SQLite3 database.

The database of choice is SQLite3 database since it is lightweight, self-container, and file-based (does not require server running to function). The SQLite3 database provides broad cross-platform functionality and portability (can be run in Windows, Linux, and Mac OS) without a lot of prior setup. However, the implementation can be easily tweaked to use different RDBMSs such as MySQL and PostgreSQL.

Scrapy would first look at the home page of [Godchecker](https://www.godchecker.com/) to find any links that leads to page describing each mythology.



## Scrapy architecture
![Scrapy architecture cannot be displayed](/scrapy_architecture_02.png "Scrapy architecture diagram")
These are the few relevant [components](https://docs.scrapy.org/en/latest/topics/architecture.html) in the implementation:
### 1. Spiders
Spiders are custom classes written byt eh users to parse responses and extract items from them or additional requests to follow. Spiders are the ones that explore the webpages for relevant information (using selectors) and send the result to the Scrapy engine as a request.
### 2. Scrapy Engine
Scrapy engine is responsible for controlling the data flow between all components of the system, and triggering events when certain actions occur. Think of it as Scrapy's brain.
### 3. Scheduler
The scheduler receives requests from the engine and enqueues them for feeding them later when the engine requests them.
### 4. Downloader
The downloader is responsible for fetching web pages and feeding them to the engine whicch, in turn feeds them to the spiders.
### 5. Item Pipeline
The Item Pipeline is responsible for processing the items once they have been extracted (or scraped) by the spiders. The tasks include cleansing, validation, and persistence (storing item to the database). This is where most processing and storage works exist.



