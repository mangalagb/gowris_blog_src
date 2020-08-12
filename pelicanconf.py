#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gowri'
SITENAME = "Gowri's Blog"
SITEURL = ""
THEME = 'themes/nest'
SITESUBTITLE = "Gowri's Personal Blog"


PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Static files
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'}
}


# Theme related settings

# Add canonical link element to top page header and all article/author/category/tag page header
NEST_REL_CANONICAL_LINK = True
# Add items to top menu before pages
MENUITEMS = [('Homepage', '/'),('Categories','/categories.html')]

NEST_HEADER_IMAGES = 'hubble.jpg'

# index.html
NEST_INDEX_HEAD_TITLE = "Homepage"
NEST_INDEX_HEADER_TITLE = "Gowri's Blog"
NEST_INDEX_HEADER_SUBTITLE = "Data Scientist & Space buff"
NEST_INDEX_CONTENT_TITLE = "Recent Posts"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)


# Social widget
SOCIAL = (('github', 'https://github.com/mangalagb'),
          ('linkedin','https://www.linkedin.com/in/mangalagowri/'))


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True