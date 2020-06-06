#from django.db import models

# Create your models here.
from django.db import models
import os

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
class Student(models.Model):
    Emails = models.EmailField(max_length=200)
    Emailt = models.EmailField(max_length=200, primary_key=True)
    Name=models.CharField(max_length=200)
    Roll = models.CharField(max_length=200)
    personID=models.CharField(max_length=200)
    Branch=models.CharField(max_length=20)
    Sem = models.CharField(max_length=20)
    Div = models.CharField(max_length=20)

# models.py
class Image(models.Model):
    Imagepath= models.ImageField(upload_to='images/')
    Emailt=models.CharField(max_length=200)
    Subject=models.CharField(max_length=50)
    Branch=models.CharField(max_length=20)
    Sem = models.CharField(max_length=20)
    Div = models.CharField(max_length=20)
    Date=models.DateField(auto_now=True)
    def filename(self):
        return os.path.basename(self.Imagepath.name)
class Signup(models.Model):
    Emailt=models.EmailField(max_length=200,primary_key=True)
    Name=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
