class SourceURLDatabase:
    """ Provides access to a database of feeds. """
    def __init__(self):
        self.urls = []

    def add(self, url, language):
        self.urls += [{'url': url, 'language': language}]

    def get(self):
        return self.urls
