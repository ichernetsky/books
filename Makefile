.PHONY: preview
preview: hakyll
	./hakyll preview

.PHONY: build
build: hakyll
	./hakyll build

hakyll: hakyll.hs
	ghc --make hakyll.hs

.PHONY: clean
clean:
	rm -Rf hakyll.hi hakyll.o _cache _site

.PHONY: clean/full
clean/full: clean
	rm -f hakyll
