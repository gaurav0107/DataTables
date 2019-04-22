from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from common.decorators import is_logged_in
from . import methods


@api_view(["POST"])
def send_mail(request):
    pass


@is_logged_in
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


def login(request):
    if request.method != "POST":
        return render(request, 'beam/login.html', context={})
    else:
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        validate_user = methods.validate_user(user_name, password)
        if validate_user['success']:
            request.session['user_id'] = validate_user['user_id']
            request.session['username'] = validate_user['username']
            request.session['email_address'] = validate_user['email_address']
            return redirect(reverse('beam:show_data'))
        else:
            return render(request, 'beam/login.html', context={})
