from django.db import models
from django.urls import reverse
import re


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#1e40af', help_text='Hex color code')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Video(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('pt', 'Portuguese'),
        ('ru', 'Russian'),
        ('ja', 'Japanese'),
        ('ko', 'Korean'),
        ('zh', 'Chinese'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    description_language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')
    youtube_url = models.URLField()
    youtube_id = models.CharField(max_length=20, blank=True)
    thumbnail_url = models.URLField(blank=True)
    code = models.TextField(help_text='Code related to this video')
    code_language = models.CharField(max_length=20, default='python', help_text='Programming language for syntax highlighting')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    leetcode_problem_number = models.IntegerField(null=True, blank=True, help_text='LeetCode problem number if applicable')
    tags = models.ManyToManyField(Tag, blank=True)
    is_featured = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.youtube_url and not self.youtube_id:
            self.youtube_id = self.extract_youtube_id()
        if self.youtube_id and not self.thumbnail_url:
            self.thumbnail_url = f'https://img.youtube.com/vi/{self.youtube_id}/maxresdefault.jpg'
        super().save(*args, **kwargs)

    def extract_youtube_id(self):
        patterns = [
            r'(?:youtube\.com\/watch\?v=)([a-zA-Z0-9_-]+)',
            r'(?:youtu\.be\/)([a-zA-Z0-9_-]+)',
            r'(?:youtube\.com\/embed\/)([a-zA-Z0-9_-]+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, self.youtube_url)
            if match:
                return match.group(1)
        return ''

    def get_absolute_url(self):
        return reverse('videos:detail', kwargs={'slug': self.slug})

    def get_embed_url(self):
        if self.youtube_id:
            return f'https://www.youtube.com/embed/{self.youtube_id}?rel=0&modestbranding=1'
        return ''

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])