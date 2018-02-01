### Author: Sonal Doomra
### UMID: 88529245
### Purpose: 507 Waiver

### Part 3: Scrape the Michigan Daily

import requests
from bs4 import BeautifulSoup


print('Michigan Daily -- MOST READ')
url = 'https://www.michigandaily.com'
r = requests.get(url)

#get beautiful soup content
soup_content = BeautifulSoup(r.content,'lxml')

#get all links to most read articles
most_Read =  soup_content.find_all(class_='view-most-read')
links_to_articles = most_Read[0].find_all('a')

#crawl through the links one level deeper to get article name and author
for link in links_to_articles:
	article = requests.get(url + link['href'])
	souptext = BeautifulSoup(article.content,'lxml')
	
	pane_entity_field = souptext.find(class_='panel-pane pane-node-title')
	article_name = pane_entity_field.h2.text
	print(article_name)
	
	byline = souptext.find(class_= 'byline')
	author = byline.find('a').text
	print('by ' + author)




