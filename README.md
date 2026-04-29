# Simple Django Blog

A full-featured blog application built with Django.
Users can register, create posts, update profiles, and interact with content through a clean UI.

##  Live Demo

https://muhamedrar.pythonanywhere.com/

##  Features

* User authentication (register, login, logout)
* Password reset via email
* Create, update, and delete posts
* User profile with image upload
* Responsive templates
* Django admin panel for management

##  Tech Stack

* Python
* Django
* SQLite (development)
* HTML, CSS

## ⚙️ Setup

```bash
git clone https://github.com/your-username/simple-django-blog.git
cd simple-django-blog
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 👤 Admin Access

Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

Then go to:
`/admin/`

## 📌 Notes

This project is deployed on PythonAnywhere and demonstrates full-stack Django development including authentication, CRUD operations, and deployment.
