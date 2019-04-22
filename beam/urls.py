from django.conf.urls import url
from beam import views

app_name = 'beam'

urlpatterns = [
    url(r'^$',
        views.show_data,
        name="show_data"),
    url(r'^login/$',
        views.login,
        name="login"),

]
