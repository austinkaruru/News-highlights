from flask import render_template
from app import app


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to News highlights 2!!'
    message = 'Ola Amigo'
    return render_template('index.html', message=message, title=title)


@app.route('/news/<int:news_id>')
def news(news_id):

    return render_template('news.html', id=news_id)
