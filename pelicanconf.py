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

PYGMENTS_STYLE = "gruvbox-light"

PLUGINS = [
    'neighbors',
    'minchin.pelican.plugins.summary',
    'render_math',
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

THEME_TEMPLATES_OVERRIDES = ["templates"]

from pathlib import Path
import re
from pybtex.database import parse_file
from pylatexenc.latex2text import LatexNodes2Text

def _person_to_string(person):
    name = " ".join(person.first_names + person.middle_names + person.last_names).strip()
    return "PS" if name == "Paul Stocker" else name

def _display_text(text):
    text = text or ""
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def _display_text(text):
    text = text or ""
    text = LatexNodes2Text().latex_to_text(text)
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def _bib_entry_order(bib_path):
    text = bib_path.read_text(encoding="utf-8")
    pattern = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
    return pattern.findall(text)


def _bib_entry_to_dict(key, entry):
    fields = dict(entry.fields)

    authors = [
        _display_text(_person_to_string(person))
        for person in entry.persons.get("author", [])
    ]

    bibtex_lines = [f"@{entry.type}{{{key},"]
    for field_name, value in fields.items():
        bibtex_lines.append(f"  {field_name:<11}= {{{value}}},")
    bibtex_lines.append("}")
    bibtex = "\n".join(bibtex_lines)

    return {
        "key": key,
        "title": _display_text(fields.get("title", "")),
        "authors": authors,
        "journal": _display_text(fields.get("journal", fields.get("booktitle", ""))),
        "journalabbr": _display_text(fields.get("journalabbr", fields.get("journal", fields.get("booktitle", "")))),
        "year": fields.get("year", ""),
        "url": fields.get("url", ""),
        "preprint": fields.get("preprint", ""),
        "slides": fields.get("slides", ""),
        "code": fields.get("code", ""),
        "bibtex": bibtex,
        "esprit": fields.get("esprit", ""),
    }


ROOT = Path(__file__).parent
BIBFILE = ROOT / "publications.bib"

_bib_data = parse_file(str(BIBFILE))
_entry_order = _bib_entry_order(BIBFILE)

PUBLICATIONS = []
for key in _entry_order:
    entry = _bib_data.entries.get(key)
    if entry is not None:
        PUBLICATIONS.append(_bib_entry_to_dict(key, entry))

JINJA_GLOBALS = {
    "PUBLICATIONS": PUBLICATIONS,
}
