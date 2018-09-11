from app import app
import urllib.request
import json
from .models import articles, sources

Sources = sources.Sources
Articles = articles.Articles

api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]
api_url = app.config["NEWS_API_URL"]


def get_news(sources):
    get_news_url = base_url.format(sources, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        sources_results = None

        if get_news_response['results']:
            sources_results_list = get_news_response['results']
            sources_results = process_results(sources_results_list)

    return sources_results


def get_news(articles):
    get_news_url = base_url.format(articles, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        articles_results = None

        if get_news_response['results']:
            articles_results_list = get_news_response['results']
            articles_results = process_results(articles_results_list)

    return articles_results


def process_results
