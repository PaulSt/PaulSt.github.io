PELICAN := $(shell command -v uv >/dev/null 2>&1 && echo "uv run pelican" || echo "pelican")

BASEDIR := $(CURDIR)
INPUTDIR := $(BASEDIR)/content
OUTPUTDIR := $(BASEDIR)/output
CONFFILE := $(BASEDIR)/pelicanconf.py
PUBLISHCONF := $(BASEDIR)/publishconf.py

PORT ?= 8000
HOST ?= 127.0.0.1

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make clean                          remove the generated files         '
	@echo '   make publish                        generate using production settings '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '                                                                          '

clean:
	rm -rf "$(OUTPUTDIR)"

publish:
	$(PELICAN) "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)"

devserver:
	$(PELICAN) -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" -b "$(HOST)" -p "$(PORT)"

.PHONY: clean publish devserver
