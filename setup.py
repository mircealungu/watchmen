from distutils.core import setup
setup(name='watchmen',
      packages=['watchmen'],
      version='0.1',
      description='Simple python library to parse and cache articles.',
      maintainer='Zeeguu',
      author="Luc van den Brand & Dan Chirtoaca",
      author_email="zeeguu_team@zeeguu.com",
      url='https://github.com/mircealungu/watchmen',
      download_url = 'https://github.com/mircealungu/watchmen/archive/0.1.tar.gz',
      keywords = ['article', 'parsing', 'caching', 'zeeguu'], 
      classifiers = [],
      install_requires=("newspaper3k==0.2.2")
      )
