import os


class Config:
    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?&apiKey={}'
    NEWS_API_ARTICLES = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = 'c076db6dfc9c4833821c0973af0d1f3e'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
