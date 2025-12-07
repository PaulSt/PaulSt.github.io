AUTHOR = 'Paul Stocker'
SITENAME = 'Paul Stocker'
SITEURL = ""

THEME = "themes/eleven-pelican-theme"
SUMMARY_MAX_LENGTH = 0
ELEVEN_LOGO='images/me.jpg'
SHOW_BANNER = True

PATH = "content"
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

PLUGINS = [
    'neighbors',
    'minchin.pelican.plugins.summary',
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('email','mailto:paul.stocker@univie.ac.at'),
        ('github','https://github.com/PaulSt'),
        ('ngstrefftz','https://paulst.github.io/NGSTrefftz/'),
         )


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
