from django.urls import path
from .views import  products, home

urlpatterns = [
    path('products/',  products, name="products"),
    path('index/',  home, name="index"), # javascript take the data from the urls of products , and pass it to his home.html
    
    
]


# serialise and get data from end point api check detail in home.html