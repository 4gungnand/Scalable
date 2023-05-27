# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import Images
 
# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Images
        fields = "__all__"