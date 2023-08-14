from django.contrib import admin
from . import models

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')

admin.site.register(models.Task, TodoAdmin)
