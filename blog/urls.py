from django.urls import path
from .views import upload, home

urlpatterns = [
    path('', upload , name="upload"),
    path('home', home , name="home")
    
]
