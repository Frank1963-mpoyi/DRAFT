from cloudinary.forms import cl_init_js_callbacks 
from django.shortcuts import render
from .models import Photo
from .forms import PhotoForm




def home (request):
    pictures = Photo.objects.get(id=4)
    context = {
        'pictures':pictures,
        'active_link':'home'
        }
    return render(request, 'pictures/index.html', context)



def upload(request):
    #context = dict( backend_form = PhotoForm())
    form = PhotoForm(request.POST, request.FILES)# mus be always on top of if above otherwise this error :local variable 'form' referenced before assignment
    if request.method == 'POST':       
        #context['posted'] = form.instance
        if form.is_valid():
            form.save()
    context = dict( backend_form = PhotoForm())# another way of difining context
    #context ={'backend_form': form}       
    return render(request, 'pictures/upload.html', context)