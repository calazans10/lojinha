clean:
	find ./ -name "*.pyc" -delete
	find ./ -name __pycache__ -delete
	-rm -rf htmlcov
	-rm -rf .coverage

deps:
	pip install -r requirements/local.txt

drop-db:
	python manage.py reset_db

create-db:
	python manage.py syncdb --noinput --migrate

setup: clean deps drop-db create-db
	python manage.py make_fixtures
	python manage.py createsuperuser --email 'admin@lojinha.com' --username 'admin'

run:
	python manage.py runserver

shell:
	python manage.py shell_plus

test:
	python manage.py test --settings=lojinha.settings.test

coverage: clean
	coverage run manage.py test --settings=lojinha.settings.test
	coverage html --include="lojinha/*"
	xdg-open htmlcov/index.html
