clean:
	rm *aux *log *lot *idx *toc *lof *out *pdf
	rm frontmatter/frontmatter.aux
	rm background/background.aux
	rm intro/intro.aux
	rm outline/outline.aux
	rm mass_model/*aux
	rm nd_sweeps/*aux
thesis:
	pdflatex --shell-escape thesis.tex

outline:
	pdflatex outline/outline.tex
