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
    pageSize = request.GET.get('limit', 10)
    pageNum = request.GET.get('page', 1)
    try:
        pageNum = int(pageNum)
    except:
        pageNum = 1
    try:
        pageSize = int(pageSize)
    except:
        pageSize = 10
    data = methods.getData(pageSize, pageNum)
    return render(request, 'beam/show_data.html', context=data)


@require_GET
def login(request):
    return render(request, 'user/login.html', context={})
