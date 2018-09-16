# from flask import render_template
# from app import app
# from flask import render_template
# from . requests import get_news, get_news1


# @app.route('/news/<int:news_id>')
# def news(news_id):

#     return render_template('news.html', id=news_id)


# @app.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data
#     '''
#     # category = get_news('business')
#     # print(category)
#     # general = get_news1('sports')
#     title = 'Home - Welcome to News highlights 2!!'
#     message = 'Ola Amigo'
#     return render_template('index.html', message=message, title=title)


# from . requests import get_news, get_news1


# # @app.route('/news/<int:news_id>')
# # def news(news_id):

# #     return render_template('news.html', id=news_id)


# # @app.route('/')
# # def index():
# #     '''
# #     View root page function that returns the index page and its data
# #     '''
# #     # category = get_news('business')
# #     # print(category)
# #     general = get_news('general')
# #     title = 'Home - Welcome to News highlights 2!!'
# #     message = 'Ola Amigo'
# #     return render_template('index.html', message=message, title=title, general=general)
