clean:
	find ./ -name "*.pyc" -delete

deps:
	pip install -r requirements.txt

setup: clean deps
	rm -rf lojinha_db
	python manage.py syncdb --noinput
	python manage.py migrate
	python manage.py make_fixtures
	python manage.py createsuperuser --email 'admin@lojinha.com' --username 'admin'

run:
	python manage.py runserver
