#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Дмитрий Кукушкин"
SITENAME = u"Simple blog"
SITEURL = u'http://xobb1t.github.com/myblog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.getpelican.com/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/xobb1t'),)

DEFAULT_PAGINATION = False

FEED_RSS = 'feeds/all.rss'
TRANSLATION_FEED = None
CATEGORY_FEED_ATOM = None

TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_STEPS = 1

THEME = 'pelican-theme'

DEFAULT_PAGINATION = 5
