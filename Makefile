mig:
	./manage.py makemigrations
	./manage.py migrate

user:
	python manage.py createsuperuser

app:
	python manage.py startapp events

