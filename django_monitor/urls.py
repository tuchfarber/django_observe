from django.urls import include, path

from django_monitor.views import glass

urlpatterns = [
    path("", glass),
]
