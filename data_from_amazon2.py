# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def price(soup):

    try:
        price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()
        #.string.strip()

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price


def rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

def review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""	

    return review_count


def availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"	

    return available

def brand(soup):
    try:
        brand = soup.find("tr", attrs={'class':'a-spacing-small po-brand'})
        brand = brand.find("span",  attrs={'class':'a-size-base po-break-word'}).string.strip()
    except AttributeError:
        brand = ""	

    return brand

def name(soup):
    try:
        
        name = soup.find("tr", attrs={'class':'a-spacing-small po-model_name'})
        name= name.find("span",  attrs={'class':'a-size-base po-break-word'}).string.strip()

    except AttributeError:
        name = ""	

    return name

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4567.89 Safari/537.36'}

URL = "https://www.amazon.pl/s?k=aparat+cyfrowy&crid=CUDJ9BA9JXT7&sprefix=aparat+%2Caps%2C118&ref=nb_sb_ss_ts-doa-p_1_7"

webpage = requests.get(URL, headers=headers)

soup = BeautifulSoup(webpage.content, "html.parser")


links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

links_list = []

for link in links:
    links_list.append(link.get('href'))

d = {"title":[], "price":[], "rating":[], "reviews":[],"availability":[], "brand":[], "name":[]}


for link in links_list:
    new_webpage = requests.get("https://www.amazon.pl" + link, headers=headers)

    soup = BeautifulSoup(new_webpage.content, "html.parser")
    d['title'].append(title(soup))
    d['price'].append(price(soup))
    d['rating'].append(rating(soup))
    d['reviews'].append(review_count(soup))
    d['availability'].append(availability(soup))
    d['brand'].append(brand(soup))
    d['name'].append(name(soup))
    
    
df = pd.DataFrame.from_dict(d)
df['title'].replace('', np.nan, inplace=True)
df = df.dropna(subset=['title'])
df.to_csv("amazon_data.csv", header=True, index=False)
    