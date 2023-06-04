from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_convert, name="index_convert"),
    path("success", views.success_convert, name="success_convert"),
]