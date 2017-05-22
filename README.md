# Watchmen
[![Build Status](https://travis-ci.org/mircealungu/watchmen.svg?branch=master)](https://travis-ci.org/mircealungu/watchmen)

A simple python library to handle online articles.

## Current features:
- Parsing the articles into a nice and readable format, determining many attributes using [newspaper](https://newspaper.readthedocs.io/en/latest/).
  - Caching these articles with a least-recently-used algorithm.
 
## Example
### Retrieving an article
To retrieve an article, you can something as follows:

```
import watchmen
article = watchmen.article_parser.get_article('http://coolarticle.nl/article.html')
print(article.title)
print(article.text)
```