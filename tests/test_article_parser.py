import time
import pytest
from watchmen.article_parser import ArticleParser

ARTICLE_URL = 'http://www.telegraaf.nl/telesport/28181735/__Bertens_simpel_door_in_Rome__.html'


@pytest.fixture
def article_parser():
    return ArticleParser()


def test_get_article(article_parser):
    """ Retrieving an article should result in non-empty content. """
    article = article_parser.get_article(ARTICLE_URL)
    assert len(article.title) > 0
    assert len(article.text) > 0


def test_get_article_cache(article_parser):
    """ The second request for the same article should be faster. """
    time_start = time.time()
    article_parser.get_article(ARTICLE_URL)
    time_passed_first_request = time.time() - time_start

    time_start = time.time()
    article_parser.get_article(ARTICLE_URL)
    time_passed_second_request = time.time() - time_start

    assert time_passed_second_request < time_passed_first_request
    print("\nTiming first call: {0:.4f} s".format(time_passed_first_request))
    print("Timing second call: {0:.4f} s".format(time_passed_second_request))