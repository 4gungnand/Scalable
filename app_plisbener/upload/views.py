from django.shortcuts import render, redirect
from .forms import GeeksForm
from .models import photos

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

    photo = photos.objects.all()
    context['photo'] = photo
    return render(request, 'index.html', context)

def success(request):
    return render(request, 'success.html')