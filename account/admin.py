from django.contrib import admin
from account.models import User, Region, TypeOfAdvice
from django.contrib.auth.models import Group

admin.site.register([User, Region, TypeOfAdvice, ])
admin.site.unregister([Group, ])
