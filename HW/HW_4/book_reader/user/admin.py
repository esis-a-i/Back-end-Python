from django.contrib import admin
from user.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    list_filter = ('first_name',)


admin.site.register(User, UserAdmin)
