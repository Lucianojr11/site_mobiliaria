from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("properties.html", views.properties, name="properties"),
    path("index.html", views.index, name="index"),
    path("property-details.html", views.properties_details, name="properties-details"),
    path("contact.html", views.contact, name="contact"),

]