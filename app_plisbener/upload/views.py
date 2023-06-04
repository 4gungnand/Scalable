from django.shortcuts import render, redirect
from .forms import GeeksForm
from .models import photos
from urllib.parse import urljoin

def index(request):
    context = {}

    if request.method == 'POST':
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            return redirect('success') 
    else:
        form = GeeksForm()
    context['form'] = form
    
    return render(request, 'index.html', context)

def success(request):
    context = {}

    photo = photos.objects.latest('id')

    url_full = photo.image.url
    img_name = url_full.split('/')[-1]
    base_url = "https://res.cloudinary.com/prema-cloud/image/upload/c_fill,h_150/"

    new_url = urljoin(base_url, img_name)

    context['photo'] = photo 
    context['img_url'] = new_url

    return render(request, 'success.html', context)