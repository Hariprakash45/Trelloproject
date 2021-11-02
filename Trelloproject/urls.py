"""Trelloproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Trelloapp.models import Trellouser
from django.contrib import admin
from django.urls import path, include                 
from rest_framework import routers                    
from Trelloapp import views    
from django.conf.urls import url      
  

app_name = "Trelloapp"
      
router = routers.DefaultRouter()      
#router.register(r'trellouser', views.Trellouser_list,basename='trellouser') 
router.register(r'categories', views.CategoriesView) 
router.register(r'task', views.TaskView)               
router.register(r'notification', views.NotificationView)    
        
urlpatterns = [
    path('admin/', admin.site.urls),           
    path('api/', include(router.urls)),
    path('api/trellouser/',views.Trellouser_list), 
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^Trelloapp/',include('Trelloapp.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    #path('task/',views.task),
    #path('categorie/',views.categorie),
    path('index/',views.index),
    

    path('trellouser_create/',views.trellouser_create),

    path('task_list/',views.task_list),
    path('task_create/',views.task_create,name='task_create'),
    path('task_read/<id>', views.task_read ),
    path('task_update/<id>', views.task_update),
    path('task_delete/<id>/', views.task_delete ),

    path('categorie_list/',views.categorie_list,),
    path('categorie_create/',views.categorie_create,name='categorie_create'),
    path('categorie_read/<id>', views.categorie_read ),
    path('categorie_update/<id>', views.categorie_update),
    path('categorie_delete/<id>/', views.categorie_delete ),
    
    path('notification/',views.notification),

]