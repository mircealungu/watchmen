from watchmen.url_list import URLList
from watchmen.curator import Curator
from watchmen.articles import Articles


class Watchmen:
    """ Provides an interface to the Watchmen package. """
    def __init__(self):
        self.urlList = URLList()
        self.curator = Curator(self.urlList)
        self.articles = Articles()
        self.urls = []
        self.refresh()

    def add_potential_urls(self, urls):
        self.urlList.add(urls)
        self.refresh()

    def good_urls(self):
        return self.urls

    def refresh(self):
        self.urls = self.curator.good_urls()
        self.articles.clear_cache()

    def articles_for_url(self, url):
        return self.articles.articles_for_url(url)

    def article_content(self, url):
        return self.articles.article_content(url)
