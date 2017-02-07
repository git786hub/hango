from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls',namespace="polls")), #namespace is included in 3 part
    url(r'^admin/', admin.site.urls),
]
