from flask import render_template
from ..requests import get_news, get_news1
from . import main


@main.route('/news/<int:news_id>')
def news(news_id):

    return render_template('news.html', id=news_id)


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # category = get_news('business')
    # print(category)
    sports = get_news1('sports')
    general = get_news1('general')
    business = get_news1('business')
    title = 'Home - Welcome to News highlights 2!!'
    message = 'Ola Amigo'
    return render_template('index.html', message=message, title=title, sports=sports, general=general, business=business)
