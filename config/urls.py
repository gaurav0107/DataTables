from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('beam.urls', namespace='beam')),
]
