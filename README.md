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

## Scrapy architecture

I chose [Scrapy](https://scrapy.org/) as one of the possible web scrapper frameworks for python, another well-known framework is [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). 
