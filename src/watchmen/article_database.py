from newspaper import Article


class ArticleDatabase:
    """ Provides access to a database of feeds. """
    def __init__(self):
        self.articles = []

    def add_article(self, source, language, article):
        row = {'article_url': article.url,
               'source_url': source.url,
               'language': language}
        self.articles += [row]

    def get_sources(self, language):
        sources = []
        for row in self.articles:
            source_language = row['language']
            source = row['source_url']
            if source_language == language and source not in sources:
                sources += [source]
        return sources

    def get_articles_for_source(self, source_url):
        source_articles = []
        for row in self.articles:
            if row['source_url'] == source_url:
                source_articles += [row]
        return source_articles

    def get_article(self, article_url):
        for row in self.articles:
            if row['article_url'] == article_url:
                language = row['language']
                article = Article(article_url, language)
                article.download()
                article.parse()
                return article

