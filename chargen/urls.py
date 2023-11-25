from django.urls import path

from . import views

app_name = "chargen"

urlpatterns = [
    path("random", views.create_character, name="create_character"),
]
