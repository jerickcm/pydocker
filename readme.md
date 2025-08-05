Tool	URL	Notes
Django	http://localhost:8000	Your Django app
Adminer	http://localhost:8080	DB web UI (lightweight)
pgAdmin	http://localhost:5050	Advanced GUI (optional)



move folder content outside

terminal:% cd pyreact 
terminal:% mv * ../
terminal:% mv .[^.]* ../
terminal:% cd ..  


add starting code project for python backend folder

docker compose run backend django-admin startproject site1 .

backend is the service name 

docker-compose exec backend python manage.py makemigrations

docker-compose exec backend python manage.py migrate


docker-compose exec backend python manage.py startapp users


python manage.py startapp users - startup is a python command 
