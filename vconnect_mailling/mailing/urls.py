from django.conf.urls import url
from vconnect_mailling.mailing import views

app_name = 'mailing'

urlpatterns = [
    url(r'^$',
        views.send_mail,
        name="send_mail"),
]
