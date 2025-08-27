from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('signup',views.signup,name='signup'),
    path('asignup',views.asignup,name='asignup'),
    path('alogin',views.alogin,name='alogin'),
    path('display/',views.display,name='display'),
    path('email',views.email,name='email'),
    path('notes',views.notes,name='notes'),
    path('imp_points',views.imp_points,name='imp_points'),
    path('viewnotes',views.viewnotes,name='viewnotes'),
    path('viewnote',views.viewnote,name='viewnote'),
    path('',views.login,name='login'),
    path('category/<str:name>/',views.category,name='category'),
    path('myupload/', views.myUpload, name='myupload'),
    path('upload/', views.uploadFile, name='upload'),
    path('pelcon/', views.PelconView.as_view(), name='pelcon'),
   
   

    
    path('pelconUpload', views.pelconUpload, name='pelconUpload'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

