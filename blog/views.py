from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post, Category


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('category').order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['featured_posts'] = Post.objects.filter(is_published=True, is_featured=True).order_by('-published_at')[:3]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('category')

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), slug=self.kwargs['slug'])
        obj.increment_view_count()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = Post.objects.filter(
            is_published=True,
            category=self.object.category
        ).exclude(id=self.object.id).order_by('-published_at')[:3]
        return context


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(
            is_published=True,
            category=self.category
        ).select_related('category').order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['all_categories'] = Category.objects.all()
        return context