# insta-hashtags

A simple tool to help generate hashtags for your Instagram posts based on categories and lists of hashtags which you define. You'll need both the front and backend servers running, as follows:

## Backend

Built with Django, and Vue for the frontend

### Setup

1. run `pipenv install` to install dependencies
2. create a MySQL database called 'hashtags'
3. update Database credentials if applicable in `insta-hashtags/settings.py`
4. run migrations with: `python3 manage.py migrate`
5. create super user with: `python3 manage.py createsuperuser`
6. run `python3 manage.py runserver`