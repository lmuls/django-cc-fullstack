Cookiecutter for creating a new project skeleton. 

Includes config for:
- Static and media files local and S3 hosting
- Ckeditor 4 with uploader for Django-admin
- Modeltranslations
- Sendgrid API library
- Whitenoise (If hosting static on same server in deployment)
- Internal / External Postgres DB with dj_database_url
- django_extensions for shell_plus ++
- Custom file for env_vars
- Custom settings (manual.py) to define db, ssl, debug based on env_var[STATE]: "DEV", "PROD"
- Procfile for hosting on Heroku

- Live reloading frontend environment with browser-sync and sass through Gulp
- Standard base template setup
- Some custom template tags
- Bootstrap
- Optional GA setup
