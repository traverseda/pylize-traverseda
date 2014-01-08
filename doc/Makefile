PYTHON = python
PY_VER = $(shell $(PYTHON) -c 'import sys;print "%i.%i" % sys.version_info[:2]')
DOCS = $(filter-out all.html, $(wildcard *.html)) logo.png css icons pylize.js
PYLIZE = ../build/scripts-$(PY_VER)/pylize

all: doc

doc: all.html $(PYLIZE)
	$(PYTHON) $(PYLIZE) -s -L ../lib

clean:
	rm -rf $(DOCS)
