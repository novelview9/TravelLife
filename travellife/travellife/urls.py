from django.conf.urls import url
from django.contrib import admin

from tmap.views import *
from tmap.api import *
from tour.views import *
from intro.views import *

from intro import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tmap/$', TmapView.as_view()),
    url(r'^address/$', AddressToPointAPIView.as_view(), name="address"),
    url(r'^tour/$', CreateAPIView.as_view()),
    url(r'^', IntroView.as_view(), name="intro"),
]
