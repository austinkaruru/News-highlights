class Config:
    NEWS_BASE_API_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_ARTICLES = 'https://newsapi.org/v2/top-headlines?sources={}apiKey={}'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
