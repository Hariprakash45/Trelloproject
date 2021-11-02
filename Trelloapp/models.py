
from django.db import models

# Create your models here.
#To store user details
class Trellouser(models.Model):
    Username = models.CharField(max_length=50)
    Emailid = models.EmailField(max_length=20)
    Password = models.CharField(max_length=20)
    def __str__(self):
        return self.Username

class Categories(models.Model):
    Categorie_Name = models.CharField(max_length=100)
    Username = models.ForeignKey(Trellouser,null=True,blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.Categorie_Name
    
#To add Tasks
class Task(models.Model):
    Username = models.ForeignKey(Trellouser,null=True,blank=True,on_delete=models.SET_NULL)
    Categorie_Name = models.ForeignKey(Categories,on_delete=models.CASCADE)
    Title = models.CharField(max_length=20)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Description = models.CharField(max_length=2000)
    def __str__(self):
        return self.Title
    
#Send notifications to user
class Notification(models.Model):
    Username = models.ForeignKey(Trellouser,null=True,blank=True,on_delete=models.SET_NULL) 
    Emailid = models.ForeignKey(Trellouser,on_delete=models.CASCADE,related_name='noticications')
    Message = models.CharField(max_length=500)
    def __str__(self):
        return self.Message 