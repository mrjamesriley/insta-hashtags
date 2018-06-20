# insta-hashtags

A simple tool to help generate hashtags for your Instagram posts based on categories and lists of hashtags which you define. You'll need both the front and backend servers running, as follows:

## Frontend

Built with Vue.js Framework

### Usage

```
cd frontend
http-server 
```

Access in browser at: `http://localhost:8080`

## Backend

Built with Django 

### Setup

1. create a MySQL database called 'hashtags'
2. update Database credentials if applicable in `backend/insta-hashtags/settings.py`
3. run migrations with: `python3 manage.py migrate`
4. create super user with: `python3 manage.py createsuperuser`
5. run `python3 manage.py runserver`