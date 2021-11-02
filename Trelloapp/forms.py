from django import forms
from .models import Task,Trellouser,Notification,Categories




class Trellouserform(forms.ModelForm):

    class Meta:
        model = Trellouser
        fields = "__all__"
        labels = {
            'Username':'',
            'Emailid':'',
            'Password':'',
        }

        widgets = {
            'Username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username', 'style': 'width: 300px;'}),
            'Emailid': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Emailid', 'style': 'width: 300px;'}), 
            'Password': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Password', 'style': 'width: 300px;'}),
        }

class Categorieform(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"
        labels = {
            'Categorie_Name':'',
            
        }
        widgets = {
            'Categorie_Name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Categorie_Name', 'style': 'width: 300px;'}),
            'Username': forms.Select(attrs={'class': 'form-control','placeholder': 'Username', 'style': 'width: 300px;'}),
        }


class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        labels = {
            
            'Title': '',
            'Start_Date': '',
            'End_Date': '',
            'Description': '',



                            
        }
        widgets = {
            'Username': forms.Select(attrs={'class': 'form-control','placeholder': 'Username', 'style': 'width: 300px;'}),
            'Categorie_Name': forms.Select(attrs={'class': 'form-control','placeholder': 'Categorie_Name', 'style': 'width: 300px;'}),
            'Title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Title', 'style': 'width: 300px;'}),
            'Start_Date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Start_Date', 'style': 'width: 300px;'}),
            'End_Date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'End_Date', 'style': 'width: 300px;'}),
            'Description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Description', 'style': 'width: 300px;'}),
        }




class Notificationform(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"
        labels = {
            'Message' : '',
        }
        widgets = {
            'Username': forms.Select(attrs={'class': 'form-control','placeholder': 'Username', 'style': 'width: 300px;'}),
            'Emailid': forms.Select(attrs={'class': 'form-control','placeholder': 'Emailid', 'style': 'width: 300px;'}), 
            'Message': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Message', 'style': 'width: 300px;'}),
        }