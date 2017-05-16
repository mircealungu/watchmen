import pytest
from watchmen.source_url_database import SourceURLDatabase
from watchmen.article_database import ArticleDatabase
from watchmen.crawler import Crawler


@pytest.fixture
def urls():
    database = SourceURLDatabase()
    database.add('http://cbs.com', 'en')
    database.add('http://tweakers.net', 'nl')
    database.add('http://www.metronieuws.nl', 'nl')
    return database


@pytest.fixture
def articles():
    return ArticleDatabase()


@pytest.fixture
def crawler(urls, articles):
    return Crawler(urls, articles)


def test_get_article(urls, articles, crawler):
    crawler.crawl()
    article = articles.get_articles_for_source('http://cbs.com')[1]
    article_text = articles.get_article(article['article_url']).text
    assert len(article_text) > 0


def test_get_articles(urls, articles, crawler):
    """Assert if we can retrieve articles from cbs. """
    assert len(articles.get_articles_for_source('http://cbs.com')) == 0
    crawler.crawl()
    assert len(articles.get_articles_for_source('http://cbs.com')) > 0
    assert len(articles.get_articles_for_source('http://cbb.com')) == 0
