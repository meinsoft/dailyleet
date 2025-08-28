from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_featured', 'reading_time', 'view_count', 'published_at')
    list_filter = ('is_published', 'is_featured', 'category', 'created_at', 'published_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('html_content', 'reading_time', 'view_count', 'created_at', 'updated_at', 'published_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'excerpt', 'category')
        }),
        ('Content', {
            'fields': ('content', 'html_content'),
            'description': 'Write your content in Markdown format. HTML preview is automatically generated.'
        }),
        ('Publishing', {
            'fields': ('is_published', 'is_featured')
        }),
        ('Statistics', {
            'fields': ('reading_time', 'view_count', 'created_at', 'updated_at', 'published_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)