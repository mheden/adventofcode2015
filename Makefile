.SILENT:
.PHONY: all format check
all:
	for file in *.py ; do \
		python3 $$file ; \
	done

format:
	black *.py

check:
	flake8 *.py
