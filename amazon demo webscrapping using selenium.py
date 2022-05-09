# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:52:36 2022

@author: shiva
"""
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from pytz import timezone 
import  csv
from datetime import datetime
import os
import time


title=[]
product_url=[] 
prices=[] 
ratings=[] 
images=[]
reviews=[]
url = f'https://www.amazon.com/s?i=specialty-aps&bbn=4954955011&rh=n%3A4954955011%2Cn%3A%212617942011%2Cn%3A2747968011&ref=nav_em__nav_desktop_sa_intl_painting_drawing_supplies_0_2_8_2'
option = webdriver.ChromeOptions()
option.add_argument('--incognito')
driver = webdriver.Chrome(r'/Users/shiva/Downloads/chromedriver_win32/chromedriver',options=option)
driver.get(url)
product=driver.find_element(By.XPATH,"//*[@id='search']/div[1]/div[1]/div/span[3]/div[2]")
p=product.find_elements(By.CLASS_NAME,'s-asin')

for p in p:

    url=p.find_element(By.TAG_NAME,'a').get_attribute('href')
    
    print(url)
    
    p_title=p.find_element(By.TAG_NAME,'h2').text

    print(p_title)
    
    image=p.find_element(By.TAG_NAME,'img').get_attribute('src')
    
    print(image)
    
    price=p.find_element(By.CLASS_NAME,'a-price').text.split()[0]
    
    print(price)
    
    review=p.find_element(By.CLASS_NAME,'a-size-small').text

    print(review)
    
    ratings_box = p.find_elements_by_xpath('.//div[@class="a-row a-size-small"]/span')
    if ratings_box != []:
            p_ratings = ratings_box[0].get_attribute('aria-label').split()[0]
            ratings.append(p_ratings)
            print(ratings)
            
    else:
            ratings = 0

    
    title.append(p_title)
    product_url.append(url)
    prices.append(price)
    
    images.append(image)
    reviews.append(review)
driver.quit()
df = pd.DataFrame({'Product Name':title,'Price':prices,'Rating':ratings,'Reviews':reviews,'Image':images,'Product_URL':product_url})
df.to_csv('products.csv', index=False, encoding='utf-8')


    
    