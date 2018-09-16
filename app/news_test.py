import unittest
from .models import Sources, Articles
Sources = sources.Sources
Articles = articles.Articles


class SourceTest(unittest.TestCase):

    def setUp(self):
        self.new_news = Sources("wee", "wewew", "Yee boiii",
                                "http://abcnews.go.com", "ayay")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, Sources))


class ArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_news = Articles("yaa", "ttt", "dee", "https://economictimes.indiatimes.com/news/defence/india-and-us-mull-working-with-oz-japan-asean-amidst-chinas-rising-influence/articleshow/65766669.cms",
                                 "https://economictimes.indiatimes.com/news/defence/india-and-us-mull-working-with-oz-japan-asean-amidst-chinas-rising-influence/articleshow/65766669.cms")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, Articles))


if __name__ == '__main__':
    unittest.main()
