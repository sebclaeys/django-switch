from django.contrib import admin
from switch.models import Switch, Group

class SwitchInline(admin.TabularInline):
    model = Switch

class GroupAdmin(admin.ModelAdmin):
    inlines = (SwitchInline,)
    
admin.site.register(Group, GroupAdmin)

