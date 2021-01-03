from django.shortcuts import render
from django.http import JsonResponse
from .models import Shirt

# endpoint Api for shirt, we will usejavascript to show this shirt
def products(request):
    shirts = Shirt.objects.all()
    data ={}
    products = []
    for shirt in shirts:
        products.append(shirt.serialize())# we append the serialize object to products empty dictionary above, shirt is variable in the for loop
    #now we must add the product to data
    data['shirts'] = products    
    return JsonResponse(data)




# THIS IS HOW JsonResponse work 
# def products(request):
#     shirts = {
#         "id": 1,
#         "brand": "Adidas",
#         "price": "2"
#     }
#     return JsonResponse(shirts)


def home (request):
    template_name ='ajax_api/home.html'
    context ={}
    return render(request, template_name, context)