from django.urls import path
from . import views

app_name = "ex01"
urlpatterns = [
    path("django", views.django_view, name="django"),
    path("display", views.display_view, name="display"),
    path("templates", views.templates_view, name="templates"),
]
