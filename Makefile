NAME := webhook-proxy-lambda
FILES := $(shell exec git ls-files)

default: test package

test:
	python *_test.py

package: dist/
	zip dist/$(NAME) $(FILES)

dist/:
	mkdir -p $@

.PHONY: package test
