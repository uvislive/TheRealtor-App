from itertools import count
from django.contrib import admin
from .models import *
# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','nickname','email')

class HomeAdmin(admin.ModelAdmin):
    list_display= ("HomeId","HomeName","HomeCat","HomePrice","HomeImage")

admin.site.register(Like)
admin.site.register(Login,LoginAdmin)
admin.site.register(Home,HomeAdmin)