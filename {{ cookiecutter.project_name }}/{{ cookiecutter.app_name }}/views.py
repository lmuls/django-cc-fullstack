
from django.shortcuts import render

from .helper import auto_generate_mail



def landing_page(request):

    context = {}
    return render(request, '{{ cookiecutter.app_name }}/landing_page.html', context)

