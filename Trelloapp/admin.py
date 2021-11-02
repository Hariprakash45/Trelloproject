from django.contrib import admin
from . models import Trellouser
from . models import Categories
from . models import Task
from . models import Notification


# Register your models here.
admin.site.register(Trellouser)
admin.site.register(Categories)
admin.site.register(Task)
admin.site.register(Notification)