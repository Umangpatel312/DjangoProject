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
    Name=models.CharField(max_length=200)
    Roll = models.CharField(max_length=200)
    personID=models.CharField(max_length=200)
# models.py
class Image(models.Model):
    img= models.ImageField(upload_to='images/')
    def filename(self):
        return os.path.basename(self.img.name)
