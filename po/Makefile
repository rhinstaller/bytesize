# Makefile for the PO files (translation) catalog

NLSPACKAGE	= bytesize
POTFILE		= $(NLSPACKAGE).pot

XGETTEXT	= xgettext --default-domain=$(NLSPACKAGE) --add-comments

PYSRC		= $(wildcard ../bytesize/*.py)
SRCFILES	= $(PYSRC)

$(POTFILE): $(SRCFILES)
	$(XGETTEXT) -L Python --keyword=_ --keyword=N_ $(SRCFILES)
	@if cmp -s $(NLSPACKAGE).po $(POTFILE); then \
            rm -f $(NLSPACKAGE).po; \
        else \
            mv -f $(NLSPACKAGE).po $(POTFILE); \
        fi; \
