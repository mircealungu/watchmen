# Watchmen
[![Build Status](https://travis-ci.org/mircealungu/watchmen.svg?branch=master)](https://travis-ci.org/mircealungu/watchmen)

An extremely simple and small python library to parse and cache online articles.

Originally designed for use in [Zeeguu](https://github.com/mircealungu/Zeeguu-Core), but can be used by anyone in need of some simple but quick caching.

## Current features:
- Parsing the articles into a nice and readable format, determining many attributes using [newspaper](https://newspaper.readthedocs.io/en/latest/).
  - Caching these articles with a least-recently-used algorithm.
 
## Example
### Retrieving an article
To retrieve an article, you can do something as follows:

```
import watchmen /* Importing automatically defines article_parser. */
article = watchmen.article_parser.get_article('http://coolarticles.nl/the_coolest_article.html')
print(article.title) 
print(article.text)
```

## Authors
Luc van den Brand, with review by Dan Chirtoaca.
Supervised by Mircea Lungu.