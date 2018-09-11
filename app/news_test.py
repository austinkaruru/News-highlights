import unittest
from models import news
News = news.news


class SourceTest(unittest.TestCase):

    def setUp(self):
        self.new_news = News("wee", "wewew", "Yee boiii",
                             "http://abcnews.go.com", "ayay")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


class ArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News("yaa", "ttt", "dee", "https://economictimes.indiatimes.com/news/defence/india-and-us-mull-working-with-oz-japan-asean-amidst-chinas-rising-influence/articleshow/65766669.cms",
                             "https://economictimes.indiatimes.com/news/defence/india-and-us-mull-working-with-oz-japan-asean-amidst-chinas-rising-influence/articleshow/65766669.cms")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


if __name__ == '__main__':
    unittest.main()
