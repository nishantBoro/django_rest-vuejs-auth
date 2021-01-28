Update(28th Jan, 2021): Updated to work with python3 and implemented registration api

# Server Setup instructions

Note: Make sure your cmd is running on this path before typing any of the commands below.
Complete the following steps:

## Update/Install python3, pip, virtualenv to latest version

## Install dependencies:

Run the following commands in command-line:
```
virtualenv -p python3 <env-name>
source <env_name>/bin/activate
pip install requirements.txt
```
Note: Tested in virtualenv with following configuration(as on 28th Jan, 2021):
      Python version: 3.6.9,
      pip version: 21.0 

## Settings.py:

Open ./DjangoRestAuth/settings.example.py
Do the manadatory changes and rename the file as settings.py

## Migrate data to your database:

This will create all the necessary tables in the database:

```
python manage.py makemigrations
python manage.py migrate
```

## Create Super-user

This will create a superuser/admin for the site:

```
python manage.py createsuperuser
.
.
python manage.py makemigrations
python manage.py migrate
```

## Create example Model objects

models.py define an example class 'Mods'. Once the client is authenticated, it can request objects of 'Mods' class and display 
it back on the client side. To do this, 'Mods' should have some objects. Let's create some:

Note: Make sure you're logged in to your database

```
python manage.py shell
from DjangoRestAuth.models import Mods
Mods.objects.create(name='put_something_here', version='put_something_here')
```

## Run development server

```
python manage.py runserver

```