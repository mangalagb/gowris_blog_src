#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gowri'
SITENAME = "Gowri's Blog"
THEME = 'themes/nest'
SITESUBTITLE = "A Personal blog of coding and travels"
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Static files
STATIC_PATHS = ['images']

##############################################################################
# Theme related settings

# Add canonical link element to top page header and all article/author/category/tag page header
NEST_REL_CANONICAL_LINK = True
# Add items to top menu before pages
MENUITEMS = [('Homepage', '/'),('Categories','/categories.html')]

NEST_HEADER_IMAGES = 'hubble.jpg'
NEST_HEADER_LOGO = '/images/g.jpg'

# index.html
NEST_INDEX_HEAD_TITLE = "Homepage"
NEST_INDEX_HEADER_TITLE = "Gowri's Blog"
NEST_INDEX_HEADER_SUBTITLE = "Data Scientist & Space buff"
NEST_INDEX_CONTENT_TITLE = "Recent Posts"

DISQUS_SITENAME = 'molivier'

##############################################################################

# Plugins
# Path to the folder containing the plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['ipynb.markup']
MARKUP = ('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"]  
#IPYNB_USE_METACELL = True
IPYNB_SKIP_CSS = True
IPYNB_FIX_CSS = True

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

##############################################################################

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Github', 'https://github.com/mangalagb'),
          ('Linkedin','https://www.linkedin.com/in/mangalagowri/'))


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True