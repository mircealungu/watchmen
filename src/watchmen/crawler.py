import newspaper


class Crawler:
    """ Provides access to a database of feeds. """
    def __init__(self, source_urls, articles):
        self.source_urls = source_urls
        self.articles = articles

    def crawl(self):
        for source_url in self.source_urls.get():
            url = source_url['url']
            language = source_url['language']
            source = newspaper.build(url, memoize_articles=False)
            for article in source.articles:
                self.articles.add_article(source, language, article)
