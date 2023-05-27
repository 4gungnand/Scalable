from django.db import models  
from django.forms import fields  
from .models import UploadImage  
from django import forms  
      
      
class UserImage(forms.ModelForm):  
    class meta:  
        models = UploadImage  
        fields = '__all__'  