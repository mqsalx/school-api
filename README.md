# school_api

py -m venv venv
venv\scripts\activate

# Permission PowerShell

Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine

# Install Django and Django REST framework into the virtual environment

pip install django
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

# Set up a new project with a single application

django-admin startproject ##### .  # Note the trailing '.' character
django-admin startapp ##### # Name of the application
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser

# Set requirements

pip freeze > requirements.txt

# Install dependencies
pip install -r requirements.txt

# Configuration of the Root Page API
pip install drf-yasg