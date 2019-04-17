from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^beam/', include('beam.urls', namespace='beam')),
]
