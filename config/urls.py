from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('beam.urls', namespace='beam')),
]
