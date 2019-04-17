from django.conf.urls import url
from beam import views

app_name = 'beam'

urlpatterns = [
    # url(r'^$',
    #     views.send_mail,
    #     name="send_mail"),
    url(r'^$',
        views.show_data,
        name="show_data")

]
