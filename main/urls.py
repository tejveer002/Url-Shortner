from django.http import HttpResponse
from django.urls import path
from main.views import routeToUrl, createurl


urlpatterns = [
    path('' ,createurl),
    path('<slug:key>' ,routeToUrl)
]
