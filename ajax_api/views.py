from django.shortcuts import render
from django.http import JsonResponse
from .models import Shirt
from django.views.decorators.csrf import csrf_exempt
# we must import to use ajax

import json # convert the requestto dictionary








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

@csrf_exempt
def home (request):
    #print(request.is_ajax()) # is to check if ajax works, it print the value True if it works
    if request.is_ajax(): # we will use this condition to get the data
        data = json.loads(request.body) # it convert request.body to dictionary # the data is store in request.body
        shirtId = data['Shid'] # shirt id call data 'Shid'
        # print(shirtId)
        shirt = Shirt.objects.get(pk=shirtId)
        visited = shirt.visited +1 # the new value of visited is the current value plus 1
        shirt.visited = visited
        shirt.save()
    template_name ='ajax_api/home.html'
    return render(request, template_name)

#THE VALUE OF VISITED CHANGED ALSO IN DATABASE


# Vue Js
# video 4 