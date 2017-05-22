from distutils.core import setup
setup(name='watchmen',
      version='0.1',
      description='Simple python library to parse articles and feeds.',
      maintainer='Zeeguu',
      author="Luc & Dan",
      author_email="zeeguu_team@zeeguu.com",
      url='https://github.com/mircealungu/watchmen',
      packages=['watchmen'],
      install_requires=("newspaper3k==0.1.9")
      )
