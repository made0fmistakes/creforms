# made by rv
from django.urls import path
from .import views

urlpatterns = [
    path('contact', views.contact),
    path('snippet',views.snippet_detail),
    path('',views.help)


]
