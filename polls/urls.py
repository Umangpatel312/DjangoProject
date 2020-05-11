from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='form'),
    path('addstudent/', views.addDetails, name='addstudent'),
    path('creategroup/', views.createGroup, name='creategroup'),
    path('addpersonfaces/', views.addPersonFaces, name='addpersonfaces'),
    path('imageupload/', views.imageUpload, name='imageupload'),
    # path('success/', views.success, name='success'),
    # path('', views.imageForm),
    # path('detectfaces/',views.detectFace,name='detectfaces'),
    # path('getspreadsheet/',views.getSpreadsheet,name='getspredsheet'),
    # path('identify/',views.identify,name='identify'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)