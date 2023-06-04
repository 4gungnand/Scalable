from django.shortcuts import render

# Create your views here.

def index_convert(request):
    return render(request, "index_convert.html")

def success_convert(request):
    return render(request, "success_convert.html")