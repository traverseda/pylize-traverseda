PY_FILES = pylize
SETUP_DIRS = build dist
PYLIZE = build/scripts/pylize
PYTHON = python
SETUP_CFG = setup.cfg

all: $(PYLIZE) doc

$(PYLIZE): $(PY_FILES) $(SETUP_CFG)
	$(PYTHON) setup.py build

$(SETUP_CFG) $(PY_FILES): pylize.in
	$(PYTHON) configure.py $(PREFIX)

install: $(PYLIZE)
	$(PYTHON) install.py

install_user: $(PYLIZE)
	$(PYTHON) install.py $(HOME)

doc:
	$(MAKE) -C doc

clean:
	rm -rf $(SETUP_DIRS) MANIFEST $(SETUP_CFG) $(PY_FILES)
	$(MAKE) -C doc clean

dist: clean
	$(PYTHON) setup.py sdist --formats=bztar,zip --no-defaults
