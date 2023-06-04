# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import photos
 
# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = photos
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data['title']
        if ' ' in title:
            raise forms.ValidationError("Title cannot contain spaces.")
        return title

    def clean_image(self):
        image = self.cleaned_data['image']
        if ' ' in image.name:
            raise forms.ValidationError("Filename cannot contain spaces.")
        return image