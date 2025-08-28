from django.contrib import admin
from .models import Profile, Experience, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'location', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'github_url', 'linkedin_url', 'twitter_url', 'youtube_url')
        }),
        ('Documents', {
            'fields': ('resume_file',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date', 'is_current', 'order')
    list_filter = ('is_current', 'start_date')
    search_fields = ('company', 'position', 'description')
    list_editable = ('order', 'is_current')
    ordering = ('order', '-start_date')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)
    list_editable = ('proficiency', 'order')
    ordering = ('category', 'order')