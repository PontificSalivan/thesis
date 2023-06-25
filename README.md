
# Инструкция по разворачиванию приложения

#### Окружение проекта:
  * python 3.8
  * Django 4.4.2
  * djangorestframework 3.14.0

#### Склонируйте репозиторий с помощью git:
```sh
git clone https://github.com/PontificSalivan/thesis
```

#### Перейдите в директорию проекта:
```sh
cd ./thesis
```
#### Создаем .env в корневой папке, пример:
```sh
DEBUG=1
SECRET_KEY=django-secret-key
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_db
SQL_USER=postgres
SQL_PASSWORD=password
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
#### Запустите команду docker:
```sh
docker-compose build
```
или
```sh
sudo docker-compose build
```
#### Создайте миграции приложения для базы данных:
```sh
docker-compose run app python manage.py migrate
```
или
```sh
sudo docker-compose run app python manage.py migrate
```
#### Создайте суперпользователя:
```sh
docker-compose run app python manage.py createsuperuser
```
или
```sh
sudo docker-compose run app python manage.py createsuperuser
```
#### Заполните поля регистрации ( почта необязательна ):
```sh
Username (leave blank to use ...): 
Email address: 
Password: 
Password (again): 
Superuser created successfully. 
```

#### Запустите приложение (localhost: http://0.0.0.0:8000/):
```sh
docker-compose up
```
или
```sh
sudo docker-compose up
```

#### Документация:
```sh
http://localhost:8000/swagger
```
```sh
ВАЖНО: Для того, чтобы пользоваться API employees нужно 
залогиниться через админку http://0.0.0.0:8000/admin/ суперпользователем созданным ранее
```