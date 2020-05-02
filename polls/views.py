from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
import cv2  # openCV
import numpy as np  # for numpy arrays
#import sqlite3
import dlib
import os,time  # for creating folders
from .models import Student
import sys
import cognitive_face as CF
import urllib
from .forms import ImageForm

def second(request):
    form = ImageForm()
    return render(request,'imageupload.html',{'form': form})
def first(request):
    return render(request,'Form.html')
def personGroupId():
    return 'test'

def addStudents(name,enroll):
    s=Student()
    print(name)
    s.Name=name
    s.Roll=enroll
    s.save()
def getPersonIdFromDatabase(roll):
    obj=Student.objects.get(Roll=roll)
    return obj.personID
def StudentAll(roll,res):
    obj=Student.objects.get(Roll=roll)
    if obj is not None:
        obj.personID=res['personId']
        obj.save()
        return True
    return False


def addDetails(request):
    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()


    name = request.GET['Name']
    roll = request.GET['Roll']
    print(name)
    print(roll)
    Id = roll[-2:]
    addStudents(name, roll)                                                  # calling the sqlite3 database


    folderName = "user" + Id                                                        # creating the person or user folder
    folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    sampleNum = 0
    while(True):
        ret, img = cap.read()                                                       # reading the camera input
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
        dets = detector(img, 1)
        for i, d in enumerate(dets):                                                # loop will run for each face detected
            sampleNum += 1
            cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg",
                        img[d.top():d.bottom(), d.left():d.right()])                                                # Saving the faces
            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
            cv2.waitKey(200)                                                        # waiting time of 200 milisecond
        cv2.imshow('frame', img)                                                    # showing the video input from camera on window
        cv2.waitKey(1)
        if(sampleNum >= 20):                                                        # will take 20 faces
            break

    cap.release()                                                                   # turning the webcam off
    cv2.destroyAllWindows()
    return render(request,'createData.html')                                               # Closing all the opened windows

def createGroup(request):

    Key = '6fe4e8e0e5074ff98c23ed2030e0a153'
    CF.Key.set(Key)
    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)
    roll=request.GET['Roll']
    if roll is not None:
        print(str('user'+roll[-2:]))
        res = CF.person.create(personGroupId(), str('user'+roll[-2:]))  # getting personid
        print(res)
        check=StudentAll(roll,res)
        if check:
            print("Person ID successfully added to the database")
            #addPersonFaces(roll)
            #train()
        else:
            print("Record doesnt found")

    return render(request,'Homepage.html')

def addPersonFaces(request):

    Key = '6fe4e8e0e5074ff98c23ed2030e0a153'
    CF.Key.set(Key)

    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)
    roll=request.GET['Roll']
    if roll is not None:
        currentDir = os.path.dirname(os.path.abspath(__file__))
        imageFolder = os.path.join(currentDir, "dataset/" + str('user'+roll[-2:]))
        person_id = getPersonIdFromDatabase(roll)
        for filename in os.listdir(imageFolder):
            if filename.endswith(".jpg"):
                print(filename)
                imgurl = os.path.join(imageFolder, filename)
                res = CF.face.detect(imgurl)
                if len(res) != 1:
                    print("No face detected in image")
                else:
                    res = CF.person.add_face(imgurl, personGroupId(), person_id)
                    print(res)
                time.sleep(6)
        train()
        return render(request,'status.html')
def train():

    Key = '6fe4e8e0e5074ff98c23ed2030e0a153'
    CF.Key.set(Key)

    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
    # https://westcentralus.api.cognitive.microsoft.com/face/v1.0/
    CF.BaseUrl.set(BASE_URL)

    res = CF.person_group.train(personGroupId())
    print(res)
    checkStatus()
def checkStatus():
    Key = '6fe4e8e0e5074ff98c23ed2030e0a153'
    CF.Key.set(Key)

    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)

    res = CF.person_group.get_status(personGroupId())
    print(res)
    # return render(request,'status.html')
def imageUpload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'imageupload.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')

