from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.first, name='form'),
    path('addstudent/', views.addDetails, name='addstudent'),
    path('addpersonfaces/', views.addPersonFaces, name='addpersonfaces'),
    path('creategroup/', views.createGroup, name='creategroup'),
    path('imageupload/', views.imageUpload, name='imageupload'),
    path('success/', views.success, name='success'),
    path('', views.second),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)