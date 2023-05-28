# from django.shortcuts import render
# from .forms import GeeksForm
 
# def index(request):
#     context ={}
 
#     # create object of form
#     form = GeeksForm(request.POST or None, request.FILES or None)
     
#     # check if form data is valid
#     if form.is_valid():
#         # save the form data to model
#         form.save()
 
#     context['form']= form
#     return render(request, "upload/index.html", context)

from django.shortcuts import render, redirect
from .forms import GeeksForm

def index(request):
    context ={}
    if request.method == 'POST':
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = GeeksForm()
    
    context['form']= form
    return render(request, 'upload/index.html', context)

def success(request):
    return render(request, 'upload/success.html')
