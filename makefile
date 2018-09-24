clean:
	rm *aux *log *lot *idx *toc *lof *out *pdf
	rm frontmatter/frontmatter.aux
	rm intro/intro.aux

thesis:
	pdflatex thesis.tex

outline:
	pdflatex outline/outline.tex
