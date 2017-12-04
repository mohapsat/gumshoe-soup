# Packages
# --Web scraping packages

from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import numpy as np

#   load URLs we want to scrape into an array
BASE_URL = 'https://www.stockgumshoe.com/most-recent-comments/'

comments = []

html = requests.get(BASE_URL).text
soup = BS(html, 'html5lib')

# print soup.prettify()

for ul_tag in soup.find_all('ul', {"class": "articles"}):
    for li_tag in ul_tag.find_all('li'):
        for div_tag in li_tag.find_all('div', {"class": "meta-info"}):
            # print div_tag.text
            comments.append(div_tag.text.encode('utf-8').strip())

comments_array = np.asarray(comments)
# print len(comments_array)

# convert to pandas dataframe
df = pd.DataFrame(comments_array)

# df.columns = ['COMMENTS']
# print df.head(10)

df.to_csv('C:/Users/smohapatra/Desktop/PROJECTS/gumshoe-soup/gumshoe_comments.csv')