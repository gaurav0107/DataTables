from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^mail/', include('mailing.urls', namespace='mailing')),
]
