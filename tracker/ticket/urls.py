from django.conf.urls import url
from views import home, ticket_listing

urlpatterns = [
    url(r'^home/$', home, name="home"),
    url(r'^home/(\w+)$', home, name="home"),
    url(r'^$', ticket_listing, name="listing")
]
