# forms.py 
from django import forms 
from .models import Image

class ImageForm(forms.Form):
	imageInput = forms.ImageField()

