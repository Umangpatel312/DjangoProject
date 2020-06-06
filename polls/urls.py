from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='form'),
    path('addstudent/', views.addStudent, name='addstudent'),
    path('creategroup/', views.createGroup, name='creategroup'),
    path('addpersonfaces/', views.addPersonFaces, name='addpersonfaces'),
    path('takeattendance/', views.imageUpload, name='takeattendance'),
    path('signup/', views.signup, name='signup'),
    # path('studentregistration/', views.studentRegistation, name='studentregistration'),
    path('login/', views.login, name='login'),
path('generateattendance/', views.generateAttendance, name='generateattendance'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)