from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news sources base url
base_url = app.config['MOVIE_BASE_URL']