from django.contrib import admin
from account.models import User, Message, State
from django.contrib.auth.models import Group
from django.forms import ModelForm

       
# @admin.register(User, Region, TypeOfAdvice)
class TheUserAdmin(admin.ModelAdmin):
    # model = User
    list_display = ('email', 'age', 'is_advisor', 'is_seeker')
    ordering = ('-id',)
    search_fields = ('email',)
    list_filter = ('is_advisor',)

admin.site.register(User, TheUserAdmin)
admin.site.register([Message, State, ])
admin.site.unregister([Group, ])
