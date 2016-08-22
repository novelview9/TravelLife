from django.conf.urls import url
from django.contrib import admin

from tmap.views import *
from tour.views import *
from intro.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tmap/$', tmap),
    url(r'^tour/$', CreateAPIView.as_view()),
    url(r'^', IntroView.as_view(), name="intro"),
    url(r'^address/$', AddressToPointView.as_view(), name="address"),
]
