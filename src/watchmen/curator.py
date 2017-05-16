class Curator:
    """ Filters feeds based on their quality"""
    def __init__(self, urlList):
        self.urlList = urlList

    def good_urls(self):
        """ Filters feeds based on their quality, constructs and returns a list. """
        urls = []
        for url in self.urlList.get():
            if self.is_readable(url):
                urls = urls + [url]
        return urls

    def is_readable(self, url):
        """ Checks if the given feed works well for readability."""
        pass
