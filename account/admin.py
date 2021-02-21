from django.contrib import admin
from account.models import User
from django.contrib.auth.models import Group
from django.forms import ModelForm

       
# @admin.register(User, Region, TypeOfAdvice)
class TheUserAdmin(admin.ModelAdmin):
    # model = User
    list_display = ('username', 'salary', 'age')
    ordering = ('-id',)
    search_fields = ('email',)

admin.site.register(User, TheUserAdmin)
admin.site.unregister([Group, ])
