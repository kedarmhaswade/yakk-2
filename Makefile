# Run all notebooks under phase-1/ after cleaning metadata
.PHONY: run-all clean-metadata

clean-metadata:
	@for f in $(shell find . -name "*.ipynb"); do \
		echo "Cleaning metadata for $$f"; \
		jq 'del(.metadata.jetTransient)' $$f > $$f.tmp && mv $$f.tmp $$f; \
	done

run-all: clean-metadata
	@for f in $(shell find phase-1 -name "*.ipynb"); do \
		echo "Running $$f"; \
		jupyter nbconvert --to notebook --execute --inplace --allow-errors $$f || exit 1; \
	done

