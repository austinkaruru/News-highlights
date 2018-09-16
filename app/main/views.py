from flask import render_template, request, redirect, url_for
from ..requests import get_news, get_articles
from . import main
from ..models import Sources, Articles


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # category = get_news('business')
    # print(category)
    # sports = get_news1('sports')
    # general = get_news1('general')
    # business = get_news1('business')
    news = get_news()
    title = 'Home - Welcome to News highlights 2!!'
    message = 'Ola Amigo'
    return render_template('index.html', message=message, title=title, sources=news)


@main.route('/articles/<string:id>')
def news(id):

    news = get_articles(id)
    print(news)

    return render_template('articles.html', articles=news)
