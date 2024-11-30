from django.urls import path

from . import views



urlpatterns = [
    path("jastindex/", views.index, name = "index"),

    path("",views.create_request, name = 'create_request'),

    path("list/", views.request_list, name = "request_list.html"),

    path("list/one_request/<int:request_id>" ,views.one_request, name = "one_request")
   
]
