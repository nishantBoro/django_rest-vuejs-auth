# Server Setup instructions

Complete the following steps:

## Install dependencies
Run the following commands in command-line(cd to ./)
```
virtualenv <env-name>
source <env_name>/bin/activate
pip install requirements.txt
```
Note:You should install virtualenv before installing the dependencies

## Settings.py

Open ./DjangoRestAuth/settings.example.py
Do the manadatory changes and rename the file as settings.py

## Migrate data to your database

```
python manage.py makemigrations
python manage.py migrate
```

## Run development server

```
python manage.py runserver

```
