from django.urls import path

from . import views

app_name = "admissions"

urlpatterns = [
    path("", views.admissions, name="admissions"),
]