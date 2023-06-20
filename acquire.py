import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

import os
from pprint import pprint



def get_all_articles(link_list):
    article_list = []
    headers = {"User-Agent": "Chrome/91.0.4472.124"}

    for links in link_list:
        for link in links:
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h1', class_='entry-title').text
            divcont = soup.find('div', class_='entry-content')
            article = [para.text for para in divcont.find_all('p')]

            article_dict = {'title': title, 'content': article}
            article_list.append(article_dict)

    return article_list

def get_news_articles():
    links = [
        'https://inshorts.com/en/read/sports',
        'https://inshorts.com/en/read/business',
        'https://inshorts.com/en/read/technology',
        'https://inshorts.com/en/read/entertainment'
    ]

    news_articles = []

    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        category = link.split('/')[-1]

        articles = soup.find_all('div', class_='news-card')

        for article in articles:
            title = article.find('span', itemprop='headline').text.strip()
            content = article.find('div', itemprop='articleBody').text.strip()

            news_articles.append({
                'title': title,
                'content': content,
                'category': category
            })

    return news_articles