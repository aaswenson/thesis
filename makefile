clean:
	rm *aux *log *lot *idx *toc *lof *out *pdf
	rm frontmatter/frontmatter.aux
	rm background/background.aux
	rm intro/intro.aux
	rm outline/outline.aux
thesis:
	pdflatex thesis.tex

outline:
	pdflatex outline/outline.tex
