from django.urls import path

from .views import image_request

app_name = 'upload_server'
urlpatterns = [
    path('', image_request, name = "image_request") 
]