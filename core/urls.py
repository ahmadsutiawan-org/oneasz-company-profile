from django.urls import path
from . import views


apps_name = "core"
urlpatterns = [
    path("", views.index, name="index"),
    # path("error/", views.error_page, name="error_page"),
    path("home/", views.home_page, name="home_page"),
    path("service/", views.service_page, name="service_page"),
    path("project/", views.project_page, name="project_page"),
    path("about/", views.about_page, name="about_page"),
    path("contact/", views.contact_page, name="contact_page"),
]
