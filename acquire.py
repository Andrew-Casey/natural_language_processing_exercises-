import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

import os
from pprint import pprint



def get_all_articles(url):
    article_list = []
    headers = {"User-Agent": "Chrome/91.0.4472.124"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the href attribute from <a> tags with class 'more-link'
    links = soup.find_all('a', class_='more-link')
    link_list = [link['href'] for link in links]

    for link in link_list:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h1', class_='entry-title').text
        divcont = soup.find('div', class_='entry-content')
        article = [para.text for para in divcont.find_all('p')]

        article_nl = ' '.join(article)

        article_dict = {'title': title, 'content': article_nl}
        article_list.append(article_dict)

    codeup_df = pd.DataFrame(article_list)

    return codeup_df

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
            
        articles_df = pd.DataFrame(news_articles)

    return articles_df