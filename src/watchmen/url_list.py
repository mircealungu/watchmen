class URLList:
    """ Provides access to a database of feeds. """
    def __init__(self):
        self.urls = []

    def add(self, new_urls):
        self.urls += [new_urls]

    def get(self):
        return self.urls
