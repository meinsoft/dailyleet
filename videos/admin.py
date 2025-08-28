from django.contrib import admin
from .models import Video, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'leetcode_problem_number', 'is_featured', 'view_count', 'created_at')
    list_filter = ('difficulty', 'is_featured', 'code_language', 'tags', 'created_at')
    search_fields = ('title', 'description', 'leetcode_problem_number')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    readonly_fields = ('youtube_id', 'thumbnail_url', 'view_count', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'description_language')
        }),
        ('YouTube Details', {
            'fields': ('youtube_url', 'youtube_id', 'thumbnail_url')
        }),
        ('Code & Difficulty', {
            'fields': ('code', 'code_language', 'difficulty', 'leetcode_problem_number')
        }),
        ('Categorization', {
            'fields': ('tags', 'is_featured')
        }),
        ('Statistics', {
            'fields': ('view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)