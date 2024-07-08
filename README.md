# Python Web Scraping Project

## About The Project:
The Drugstore Product Scraper is a comprehensive project designed to automate the process of logging into Rossmann's website, scraping product information from various categories, and cleaning the data for further analysis. This project uses Selenium for web automation, Scrapy for crawling, BeautifulSoup for web scraping, and Pandas for data manipulation.

## Steps

### 1. Logging into the Drugstore's Website:
This script uses Selenium to automate the login process on the Drugstore's website.

### 2. Collecting Product Category Links:
This script uses a Scrapy webcrawler to collect links to product categories from the Drugstore's website.

### 3. Scraping Products: 
This script scrapes product information separately for both male and female categories using BeautifulSoup. Labeling each product, whether they are for women or men is neccessary to carry out further analysis on the presence of "Pink Tax" in Poland.

The following product data is scrapped:
- Product Name
- Price
- Gender
- Product Category
- Product Sub Category
- Product Size

Total Number of Products Scrapped: 12 550

### 4. Data Cleaning:
As a last step, the script cleans the scrapped data to make it ready for further analysis 

### Final Output:
![Screen Shot 2024-07-08 at 12 22 49](https://github.com/wick404/Webscraping_Drugstore/assets/173910609/ba3f1ded-e0a0-40c9-9164-4721d69d25da)

## Prerequisites:
- Knowledge of Python programming.
- Understanding of web scraping techniques.
- Familiarity with Selenium, Scrapy, BeautifulSoup, and Pandas.
- ChromeDriver for Selenium.

## Python packages used:
- selenium
- scrapy
- beautifulsoup4
- pandas
- requests
- re

## Possible Further Work:
Based on the collected data, the presence of "Pink Tax" in Poland could be analyzed.

