from django.conf.urls import url
from user import views

app_name = 'user'
url(r'^login/$',
    views.login,
    name="login"),
