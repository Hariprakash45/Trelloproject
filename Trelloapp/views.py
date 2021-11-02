from django.db.models.query import QuerySet
from Trelloapp import forms
from Trelloapp.forms import Trellouserform,Taskform,Categorieform,Notificationform
from Trelloapp import serializers
from Trelloapp.serializers import TaskSerializers,TrellouserSerializers,NotificationSerializers,CategoriesSerializers
from .models import Task,Trellouser,Notification,Categories
from rest_framework import viewsets    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect,render,HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

def index(request):
    return render(request,'index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = Trellouserform(data=request.POST)
    
        if user_form.is_valid():
            user = user_form.save()
            Username = user_form.cleaned_data['Username']
            Password = user_form.cleaned_data['Password']
            user.save()
            user = authenticate(username=Username, password=Password)
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = Trellouserform()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(username=Username, password=Password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/categorie_create/")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(Username,Password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})



#CRUD OPERATIONS USING DJANGO TEMPLATES#

def trellouser_create(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    trellouser_form = Trellouserform(request.POST or None)
    if trellouser_form.is_valid():
        trellouser_form.save()
        return HttpResponseRedirect("/categorie_create/")
         
    context['trellouser_form']= trellouser_form
    return render(request, "trellouser_create.html", context)

@csrf_exempt
def task_list(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Task.objects.all()
         
    return render(request, "task_list.html", context)

@csrf_exempt
def task_create(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    task_form = Taskform(request.POST or None)
    if task_form.is_valid():
        task_form.save()
        return HttpResponseRedirect("/index/")
    context['task_form']= task_form
    return render(request, "task_create.html", context)

@csrf_exempt
def task_read(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Task.objects.get(id = id)
         
    return render(request, "task_read.html", context)

@csrf_exempt
def task_update(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Task, id = id)
 
    # pass the object as instance in form
    task_form = Taskform(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if task_form.is_valid():
        task_form.save()
        return HttpResponseRedirect("/task_list/")
 
    # add form dictionary to context
    else:
      context["task_form"] = task_form
 
    return render(request, "task_update.html", context)

@csrf_exempt
def task_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Task, id = id)
    context["data"] = Task.objects.get(id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "task_delete.html", context)


@csrf_exempt
def categorie_list(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Categories.objects.all()
         
    return render(request, "categorie_list.html", context)

@csrf_exempt
def categorie_create(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    categorie_form = Categorieform(request.POST or None)
    
    if categorie_form.is_valid():
        categorie_form.save()
    

        return HttpResponseRedirect("/task_create/")

    else:     
       context['categorie_form']= categorie_form
       
       
    return render(request, "categorie_create.html", context)

@csrf_exempt
def categorie_read(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Categories.objects.get(id = id)
         
    return render(request, "categorie_read.html", context)

@csrf_exempt
def categorie_update(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Categories, id = id)
 
    # pass the object as instance in form
    categorie_form = Categorieform(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if categorie_form.is_valid():
        categorie_form.save()
        return HttpResponseRedirect("/categorie_list/")
 
    # add form dictionary to context
    else:
      context["categorie_form"] = categorie_form
 
    return render(request, "categorie_update.html", context)

@csrf_exempt
def categorie_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Categories, id = id)
    context["data"] = Categories.objects.get(id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
   
    return render(request, "categorie_delete.html", context)

@csrf_exempt
def notification(request):
    if request.method == "POST":
        notification_form = Notificationform(request.POST)
        if notification_form.is_valid():
           notification_form.save(commit=True)
        return HttpResponse("<h2>Notification sent</h2>")
    else:
            notification_form = forms.Notificationform()
    return render(request,'notification.html',{'notification_form':notification_form})


#CRUD OPERATIONS API'S USING DJANGO RESTFRAMEWORK

@api_view(['POST'])
def Trellouser_list(request):
    if request.method == 'POST':
        serializer = TrellouserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:    
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesView(viewsets.ModelViewSet):
        serializer_class = CategoriesSerializers          
        queryset = Categories.objects.all()

class TaskView(viewsets.ModelViewSet):
         serializer_class = TaskSerializers          
         queryset = Task.objects.all()


class NotificationView(viewsets.ModelViewSet):
         serializer_class = NotificationSerializers         
         queryset = Notification.objects.all()









