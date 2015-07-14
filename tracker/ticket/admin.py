from django.contrib import admin
from models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule_date', 'colored_due_date')


admin.site.register(Task, TaskAdmin)
