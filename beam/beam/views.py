from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.views.decorators.http import require_GET

from . import methods


@api_view(["POST"])
def send_mail(request):
    pass


@require_GET
def show_data(request):
    data = methods.get_data()
    return render(request, 'beam/show_data.html', context=data)
