from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name = "index"),

    path("request/",views.create_request, name = 'create_request'),

    path("list/", views.request_list, name = "request_list.html")
   
]
