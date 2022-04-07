# crime-file-management
Crime file reporting process and management and digitalize the government facilities for residents of any country


## Setup
#### The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Bappy4u/crime-file-management.git
$ cd storefront
```

#### Create a virtual environment to install dependencies in and activate it:
if you have `pipenv`  installed in your machine
```sh
$ pipenv install
```
It will install a virtual environment for you and will install all the dependencies
* Select that environment as your python interpreter

* To migrate all the settings command this in the terminal
```sh
(crime-file-management)$ python manage.py migrate
```

* To check the admin pannel create a super user

```sh
(crime-file-management)$ python manage.py createsuperuser
```

* Finally 

```sh
(crime-file-management)$ python manage.py runserver
```
And navigate to http://127.0.0.1:8000/


#### What I've used in this project
* Python 3.8
* Django 3.2.5
* Django-orm
* MySql
* django-debug-toolbar
* django-rest-framework (not used yet)

#### Incomplete task
* Announcement app
* Missing person app
* Front-end with React



