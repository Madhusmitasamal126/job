from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_by', 'posted_on')
    search_fields = ('title', 'company', 'location', 'description')
    list_filter = ('posted_by', 'posted_on')
    ordering = ('-posted_on',)
