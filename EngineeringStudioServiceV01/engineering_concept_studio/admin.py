from django.contrib import admin

from .models import *

@admin.register(Project)
class ProjectActionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Assembly)
class AssemblyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project')