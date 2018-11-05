

pdf:
	pdflatex --shell-escape thesis && \
	bibtex thesis && \
	pdflatex --shell-escape thesis && \
	pdflatex --shell-escape thesis

preview: pdf
	evince thesis.pdf 

clean:
#	git clean -dfx .
