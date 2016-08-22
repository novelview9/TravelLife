from django.conf.urls import url
from django.contrib import admin
from . import views

from tmap.views import *
from tour.views import *
from intro import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tmap/$', tmap),
    url(r'^tour/$', CreateAPIView.as_view()),
    url(r'^', views.IntroView.as_view(), name="intro"),
    url(r'^address/$', AddressToPointView.as_view(), name="address"),
]
