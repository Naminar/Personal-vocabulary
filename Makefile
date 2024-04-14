
all: install
	git submodule update --init

install:
	pip3 install colored
	pip install python-docx
	pip install pypdf
	pip install termcolor
	pip install regex