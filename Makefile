all: clean build deploy

install:
	pipenv install

build:
	pipenv run pyinstaller --onefile pywhitenoiseweb.py -n pywhitenoiseweb-dynamic
	pipenv run staticx dist/pywhitenoiseweb-dynamic dist/pywhitenoiseweb

run:
	pipenv run python pywhitenoiseweb.py

run-build:
	dist/pywhitenoiseweb/pywhitenoiseweb

clean:
	rm -fr build dist pywhitenoiseweb.spec

deploy:
	test -e deploy.sh && ./deploy.sh
