from django.conf.urls import url
from views import home

urlpatterns = [
       url(r'^home/(\w+)', home, name="home")
]
