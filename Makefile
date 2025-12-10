PELICAN := $(shell command -v uv >/dev/null 2>&1 && echo "uv run pelican" || echo "python3 -m pelican")

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

clean:
	rm -rf $(OUTPUTDIR)
publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF)
serve:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) -b 0.0.0.0 -p 8000

.PHONY: clean publish serve
