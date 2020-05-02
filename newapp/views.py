from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'Form.html')

def result(request):
    user_input=request.GET['user_input']
    return render(request,'createData.html',{'input':user_input})