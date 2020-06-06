# forms.py 
from django import forms 
from .models import Image
from .models import Signup
class ImageForm(forms.Form):
	imageInput = forms.ImageField()
	subject = forms.CharField()
	branch = forms.CharField()
	sem = forms.CharField()
	div = forms.CharField()
class SignupForm(forms.Form):
	emailt=forms.EmailField()
	name=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

class StudentForm(forms.Form):
	emails=forms.EmailField()
	name=forms.CharField()
	roll = forms.CharField()
	branch = forms.CharField()
	sem = forms.CharField()
	div = forms.CharField()
class LoginForm(forms.Form):
	emailt=forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
class GenerateAttendance(forms.Form):
	branch=forms.CharField()
	sem=forms.CharField()
	div=forms.CharField()
	subject=forms.CharField()
