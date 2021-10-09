from django.urls import path

from {{ cookiecutter.app_name }}.views import landing_page

urlpatterns = [
    path('', landing_page, name="landing_page"),
]