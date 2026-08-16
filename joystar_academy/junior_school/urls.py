from django.urls import path

from . import views

app_name = "junior_school"

urlpatterns = [
    path("", views.junior_school, name="junior_school"),
]