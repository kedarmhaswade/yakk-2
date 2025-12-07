# Clean notebook metadata
clean-metadata:
	@echo "Cleaning transient metadata in notebooks..."
	@for f in $(NOTEBOOKS); do \
	    echo "Cleaning metadata for $$f"; \
	    jq 'del(.metadata.jetTransient)' $$f > $$f.tmp && mv $$f.tmp $$f; \
	done


# Makefile for yakk-2 blog

PYTHON := python3
BUILD_SCRIPT := build_script.py
POSTS_DIR := posts
OUTPUT_DIR := blog

.PHONY: all build clean

all: build

# Build blog HTML from notebooks
build:
	$(PYTHON) $(BUILD_SCRIPT)

# Clean generated HTML files
clean:
	rm -rf $(OUTPUT_DIR)/*.html

