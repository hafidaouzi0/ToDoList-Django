from django.contrib import admin
from .models import ToDoList,Item

# Register your models here.
#to make the dashboard access the database or basically 
#to be able to see our todolists in the admin site
#remeber: if you create a new model you should register that from admin.py file

admin.site.register(ToDoList)
admin.site.register(Item)
