from url_list import URLList
from curator import Curator
from articles import Articles


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
        self.urls = self.curator.goodUrls()
        self.articles.clean()

    def articles_for_url(self, url):
        return self.articles.articles_for_url(url)

    def article_content(self, articleURL):
        return self.articles.article_content(articleURL)
