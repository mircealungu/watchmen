from newspaper import Article
from watchmen.cache import LRUCache


class ArticleParser:
    """ Downloads and analyses articles, stores them in cache for efficient retrieval. """

    CACHE_SIZE = 1000

    def __init__(self, cache_size = CACHE_SIZE):
        """ Initialises the cache, where cache size is CACHE_SIZE by default. """
        self.articleCache = LRUCache(cache_size)

    def get_article(self, article_url):
        """ Downloads and parses an article based on the url, or retrieves it from cache. 
            Uses the newspaper library to filter out any clutter. """
        article = self.articleCache.get(article_url)

        if not article:
            article = Article(article_url)
            article.download()
            article.parse()
            self.articleCache.set(article_url, article)

        return article
