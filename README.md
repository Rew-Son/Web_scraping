# Amazon Product Scraper

## Overview

Welcome to the Amazon Product Scraper, a Python script designed to extract product information from Amazon's search results. This script, powered by BeautifulSoup and requests, provides a convenient way to gather data on titles, prices, ratings, reviews, availability, brand, and product names.

## Prerequisites

Before diving into the world of Amazon scraping, ensure you have the following enchantments:

- Python 3.x
- Essential Python scrolls (install using `pip install scroll_name`):
  - beautifulsoup4
  - requests
  - pandas
  - numpy

## Usage

1. Brew a concoction of required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```
2. Invoke the script
   ```bash
   pip install -r requirements.txt
   ```
3. Explore Amazon's massive dataset, collecting data on various products.
4. The generated "amazon_data.csv" file, which is a set of product information, will be the basis for further price analyzes and detailed parameters.
## Script Details
### Functions
  * #### title
     Extracts the title of the product from the Amazon product page.
  * #### price
    Extracts the price of the product, considering deal prices if available.
  * #### rating
    Extracts the product rating, handling variations in HTML structure.
  * #### review_count
    Extracts the number of customer reviews for the product.
  * #### availability
    Determines the availability status of the product.
  * ####  brand
    Extracts the brand of the product.
  * ####  name
    Extracts the name of the product.

### How it Works
1. Sends a request to the Amazon search page.
2. Extracts links to individual product pages from the search results.
3. Iterates through each product page, extracting relevant information using the defined functions.
4. Creates a pandas DataFrame with the collected data.
5. Cleans the data by dropping rows with missing titles.
6. Saves the final dataset as "amazon_data.csv."
