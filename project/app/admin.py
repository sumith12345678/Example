from django.contrib import admin
from . models import *



@admin.register(Book)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id','Book_name','image','price','category','Author','status')
    

# Register your models here.
