from django.db import models
from django.urls import reverse
from django.utils import timezone
import markdown
from markdown.extensions import codehilite


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(max_length=300, help_text='Short description for the post card')
    content = models.TextField(help_text='Write your post in Markdown format')
    html_content = models.TextField(blank=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    reading_time = models.PositiveIntegerField(default=0, help_text='Estimated reading time in minutes')
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.content:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.tables'
            ])
            self.html_content = md.convert(self.content)
            
            # Calculate reading time (average 200 words per minute)
            word_count = len(self.content.split())
            self.reading_time = max(1, round(word_count / 200))
        
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        elif not self.is_published:
            self.published_at = None
            
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])