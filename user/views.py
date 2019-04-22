from django.shortcuts import render, redirect
from django.urls import reverse

from user import methods


def login(request):
    if request.method != "POST":
        return render(request, 'user/login.html', context={})
    else:
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        validate_user = methods.validate_user(user_name, password)
        if validate_user['success']:
            request.session['user_id'] = validate_user['user_id']
            request.session['username'] = validate_user['username']
            request.session['email_address'] = validate_user['email_address']
        return redirect(reverse('beam:show_data'))
