import os

import dj_database_url


def define_debug():
    state = os.environ.get("STATE")

    if state == "DEV":
        return True
    elif state == "PROD":
        return False
 
def define_db():
    state = os.environ.get("STATE")
    use_db = os.environ.get("USE_DB")

    if state == "DEV" and use_db == "EXTERNAL":
        db = dj_database_url.config(conn_max_age=600, ssl_require=True)
        print("Using external DB")
        return db

    elif state == "DEV" and use_db == "LOCAL":
        db = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '{{cookiecutter.project_name}}_dev',
            'USER': 'postgres',
            'PASSWORD': 'ragopass123'
        }
        print("Using local DB")
        return db

    elif state == "PROD":
        db = dj_database_url.config(conn_max_age=600, ssl_require=True)
        print("Using external DB")
        return db

    else:
        print('None of the db possibilities matched')
        return None


def define_ssl():
    state = os.environ.get("STATE")
    if state == "DEV":
        return False
    elif state == "PROD":
        return True
    else: 
        return f'define_ssl failed, envvariable "STATE" didnt match.'    