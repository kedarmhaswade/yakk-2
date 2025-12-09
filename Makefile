.PHONY: all clean-metadata

# Phases
PHASES := phase-1 phase-2 phase-3 phase-4 phase-5

# Find all notebooks
ALL_NB := $(shell find $(PHASES) -name "*.ipynb")

# Default target: execute only notebooks that have no outputs
all:
	@echo ">>> Executing notebooks that are not yet executed..."
	@for nb in $(ALL_NB); do \
		has_output=$$(python3 -c "import nbformat; nb=nbformat.read('$$nb', as_version=4); print(any(len(cell.get('outputs', []))>0 for cell in nb.cells))"); \
		if [ "$$has_output" = "False" ]; then \
			echo ">>> Executing $$nb"; \
			jupyter nbconvert --to notebook --inplace \
				--ExecutePreprocessor.timeout=300 \
				--ExecutePreprocessor.allow_errors=True \
				$$nb || true; \
		else \
			echo ">>> Skipping $$nb (already executed)"; \
		fi \
	done
	@echo ">>> Done executing notebooks."

# Clean transient metadata from all notebooks in phases
clean-metadata:
	@echo ">>> Cleaning metadata from notebooks in phase-1 to phase-5..."
	@for nb in $(ALL_NB); do \
		echo ">>> Cleaning metadata in $$nb"; \
		nbstripout $$nb; \
	done
	@echo ">>> Done cleaning metadata."

