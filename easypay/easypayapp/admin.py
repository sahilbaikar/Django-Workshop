from django.contrib import admin

from .models import Userprofile,Transaction 

# # Register your models here.

admin.site.register(Userprofile )
admin.site.register(Transaction )

