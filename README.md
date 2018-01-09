# Django 1.11
Hello there,

Welcome to my github. I am Suveen.

## CRUD App
This is a basic Django CRUD Application. The following are the basic commands to start django application.

## 1. Create Dev Directory for General Project Storage

    cd ~/
    mkdir Dev && cd Dev
##  2. Create Virtual Environment

    cd ~/Dev
    mkdir cfehome && cd cfehome
    virtualenv -p python3 .
    
    # activate on Mac/Linux
    source bin/activate
    
    # activate on Windows
    .\Scripts\activate
## 3. Install Django & Start Project

    pip install django==1.11.8
    mkdir src && cd src
    django-admin.py startproject cfehome .
    # Windows (optional)
    .\Scripts\django-admin.py startproject cfehome .
## 4. Create New Settings Module
The purpose of this is to create a settings module that works for both local and production use. This is not a requirement but is highly recommended.

    # currently working in
    # ~/Dev/cfehome/src/ on mac/linux
    # \Users\YourName\Dev\cfehome\src on windows
    cd cfehome
    mkdir settings && cd settings
Create **__init__.py** within new Settings folder to make it a module. Add the following:

    # currently working in
    # ~/Dev/cfehome/src/cfehome/settings/ on mac/linux
    # \Users\YourName\Dev\cfehome\src\cfehome\settings\ on windows
    echo "from .base import *
    from .production import *
    try:
	    from .local import *
    except: 
	    pass
	" > __init__.py
Change **BASE_DIR** in **settings.py** :

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # to
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Move default **settings.py** into new settings module and rename **settings.py** to **base.py** :

    # mac/linux
    mv ~/Dev/cfehome/src/cfehome/settings.py
    ~/Dev/cfehome/src/cfehome/settings/base.py
    # windows
    move \Users\YourName\Dev\cfehome\src\cfehome\settings.py
    \Users\YourName\Dev\cfehome\src\settings\base.py
Copy Local settings (local.py) to make new (base.py & production.py) File:

    # mac/linux
    cp ~/Dev/cfehome/src/cfehome/settings/base.py
    ~/Dev/cfehome/src/cfehome/settings/local.py
    cp ~/Dev/cfehome/src/cfehome/settings/base.py
    ~/Dev/cfehome/src/cfehome/settings/production.py
    #windows
    copy \Users\YourName\Dev\cfehome\src\cfehome\settings\base.py
    \Users\YourName\Dev\cfehome\src\cfehome\settings\local.py
    copy \Users\YourName\Dev\cfehome\src\cfehome\settings\base.py
    \Users\YourName\Dev\cfehome\src\cfehome\settings\production.py
## 5. Some other common installations (optional):

    # for a postgresql database
    pip install psycopg2
    # for a mysql database
    pip install mysqlclient #python3
    pip install MySQL-python #python2
    # for use on heroku
    pip install gunicorn dj-database-url
    pip install django-crispy-forms
    pip install pillow
## 6. Create requirements.txt File

    pip freeze > requirements.txt
## 7. Run Migration & Createsuperuser

    python manage.py migrate
    python manage.py createsuperuser
## 8. Run the Server

    python manage.py runserver
