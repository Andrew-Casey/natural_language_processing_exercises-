import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

import unicodedata
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import pandas as pd

import os
from pprint import pprint 
import acquire as a

def basic_clean(text):
    # Lowercase everything
    text = text.lower()
    
    # Normalize unicode characters
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    # Replace anything that is not a letter, number, whitespace, or a single quote
    text = re.sub(r"[^a-zA-Z0-9\s']", '', text)
    
    return text

def tokenize(text):
    # Tokenize all the words in the string
    tokens = nltk.word_tokenize(text)
    return ' '.join(tokens)

def stem(text):
    # Apply stemming to all the words
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in text.split()]
    return ' '.join(stemmed_words)

def lemmatize(text):
    # Apply lemmatization to each word
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text.split()]
    return ' '.join(lemmatized_words)

def remove_stopwords(text, extra_words=[], exclude_words=[]):
    # Remove stopwords from the text
    stopword_list = stopwords.words('english')
    stopword_list.extend(extra_words)
    stopword_list = [word for word in stopword_list if word not in exclude_words]
    words = text.split()
    filtered_words = [word for word in words if word not in stopword_list]
    return ' '.join(filtered_words)

