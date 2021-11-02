from rest_framework import serializers
from . models import Categories
from . models import Task
from . models import Trellouser
from . models import Notification

class TrellouserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trellouser
        fields = ("Username","Emailid","Password")

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ("Categorie_Name","Username")

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("Username","Categorie_Name","Title","Start_Date","End_Date","Description")

class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("Username","Emailid","Message")