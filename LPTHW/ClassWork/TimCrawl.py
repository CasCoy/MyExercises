
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:20:04 2017

@author: Tim
"""


import requests  #responsible for getting the HTML Code
from unicode import BeautifulSoup #converts code into text
from urllib.parse import urljoin #helpful to use relative URLs
import csv #needed for writing crawled elemts into a csv file

#creating an object that contains the different objects
class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image

#creating object that is actual crawler
class ArticleFetcher():
    def fetch(self):
        articles = []
        url = "http://python.beispiel.programmierenlernen.io/index.php"         #URL to be crawled

        while url != "":                                                        #while loop to get additional websites
            r = requests.get(url)                                               #getting the code
            doc = BeautifulSoup(r.text, "html.parser")                          #parsing of code into text
            for card in doc.select(".card"):                                    #for loop to create different attributes for crawled objects
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])

                crawled = CrawledArticle(title, emoji, content, image)
                articles.append(crawled)

            next = doc.select_one(".navigation .btn")                           #responsible for crawling next pages
            if next:
                next_href = urljoin(url, next.attrs["href"])
                url = next_href
            else:
                url=""

        return articles

fetcher = ArticleFetcher()
articles = fetcher.fetch()

with open ("Results.csv", "w", newline = "") as csvfile:                          #writing of objects into csv file
    writer = csv.writer(csvfile, delimiter=";", quotechar='"')
    for article in articles:
        writer.writerow([article.title, article.emoji, article.image, article.content])


# You can also just print the different object attributes#

for article in articles:
    print(article.emoji)
