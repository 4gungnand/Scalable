from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from upload_server.forms import UserImage

from .models import *

def image_request(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'index.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImage()  
        return render(request, 'index.html', {'form':form})