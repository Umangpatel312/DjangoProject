from .forms import *
from .models import *
def personGroupId():
    return 'test'
def studentEmailExist(emails):
    try:
        obj = Student.objects.get(Emails=emails)
    except:
        obj=None
    if obj is None:
        return False
    return True

def teacherEmailExist(email):

    try:
        obj = Signup.objects.get(Emailt=email)
    except:
        obj=None
    if obj is None:
        return False
    return True

def getPersonIdFromDatabase(roll):
    obj=Student.objects.get(Roll=roll)
    return obj.personID

def getDataUsingPersonId(personId,branch,sem,div):
    try:
        print(personId,branch,sem,div)
        obj=Student.objects.get(personID=personId,Branch=branch,Sem=sem,Div=div)
        # print("object")
    except:
        obj = None
        print("none")
    return obj

def selectStudent():
    return Student.objects.all()

def updatePersonId(roll,res):
    obj=Student.objects.get(Roll=roll)
    if obj is not None:
        obj.personID=res['personId']
        obj.save()
        return True
    return False

def countStudent():
    return Student.objects.count()

