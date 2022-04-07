# crime-file-management
Crime file reporting process and management and digitalize the government facilities for residents of any country


#### 1.1	Introduction
Online crime file management system provides facility for reporting online crimes, complaints, wanted persons list, various announcement for the particular locality with multimedia content (videos, pictures, verbal). This system will allow user to sign up and enter a complaint or register a grievance with enough evidence. Administrator from the National Authority will verify and take necessary steps. The users who complains will see the status or the actions taken from the authority on the complaints. To ensure security the complaints will only accessible by the authority and the complainer himself, no one outside this two can access complaints and crime report. 

#### 1.2	Purpose of the project
This system will help people to reduce sufferings to complaints and register grievance against crime. It will help to track the status about the complaints. The authority will also can provide various announcement for the particular locality if they want to. This is reduce the gap between the National Authority and Citizens of any country.

![image](https://user-images.githubusercontent.com/26277680/162214292-bd2e8b77-ac56-4e92-9904-81427b01ac39.png)

#### Data flow diagram
![image](https://user-images.githubusercontent.com/26277680/162215216-b71e5e3f-7819-4d69-b82e-550c31bfa501.png)


#### Data Dictionary
![image](https://user-images.githubusercontent.com/26277680/162214761-16650b70-ea48-4b45-8213-b5051ca605bf.png)

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



