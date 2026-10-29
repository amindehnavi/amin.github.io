# Build commands for the bilingual site. Run `make help` for the list.
PY ?= .venv/bin/python

# Use the project virtualenv for Quarto's Jupyter kernel when it exists.
ifneq ($(wildcard .venv/bin/python),)
export QUARTO_PYTHON := $(abspath .venv/bin/python)
endif

.PHONY: help sync preview-en preview-fa render-en render-fa clean

help:
	@echo "make sync        copy shared/ into en/assets and fa/assets"
	@echo "make preview-en  live preview of the English site"
	@echo "make preview-fa  live preview of the Persian site"
	@echo "make render-en   render the English site into en/_site"
	@echo "make render-fa   render the Persian site into fa/_site"
	@echo "make clean       delete all build output"

sync:
	$(PY) scripts/sync_shared.py

preview-en: sync
	quarto preview en

preview-fa: sync
	quarto preview fa

render-en: sync
	quarto render en

render-fa: sync
	quarto render fa

clean:
	rm -rf public en/_site fa/_site en/assets fa/assets en/.quarto fa/.quarto
