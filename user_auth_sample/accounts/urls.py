from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^profile/$', user_profile, name = 'user_profile'),
]
