from django.conf.urls import url
from views import home, ticket_listing, ticket_list, ticket_detail

urlpatterns = [
    url(r'^home/$', home, name="home"),
    url(r'^home/(\w+)$', home, name="home"),
    url(r'^$', ticket_listing, name="listing"),
    url(r'^list/$', ticket_list, name="list"),
    url(r'^detail/(\d+)', ticket_detail, name="detail")
]
