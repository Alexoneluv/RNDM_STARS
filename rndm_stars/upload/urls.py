from django.urls import path
from .views import upload_nature

urlpatterns = [
    path('upload/nature/', upload_nature, name='upload_nature'),
]