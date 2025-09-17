from django.contrib import admin
from .models import CandidateProfile, JobApplication

@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'skills_preview', 'resume_link')
    search_fields = ('user__username', 'user__email', 'skills', 'phone')
    list_filter = ('user',)
    ordering = ('user__username',)

    def skills_preview(self, obj):
        return obj.skills[:50] + "..." if obj.skills else "-"
    skills_preview.short_description = "Skills"

    def resume_link(self, obj):
        if obj.resume:
            return f'<a href="{obj.resume.url}" target="_blank">View</a>'
        return "-"
    resume_link.allow_tags = True
    resume_link.short_description = "Resume"

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'applied_on', 'resume_link')
    list_filter = ('status', 'job')
    search_fields = ('user__username', 'job__title', 'status')
    ordering = ('-applied_on',)

    def resume_link(self, obj):
        if obj.resume:
            return f'<a href="{obj.resume.url}" target="_blank">View</a>'
        return "-"
    resume_link.allow_tags = True
    resume_link.short_description = "Resume"
