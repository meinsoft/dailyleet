from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Video, Tag


class VideoListView(ListView):
    model = Video
    template_name = 'videos/list.html'
    context_object_name = 'videos'
    paginate_by = 12

    def get_queryset(self):
        return Video.objects.prefetch_related('tags').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/detail.html'
    context_object_name = 'video'

    def get_object(self):
        obj = get_object_or_404(Video, slug=self.kwargs['slug'])
        obj.increment_view_count()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_videos'] = Video.objects.filter(
            tags__in=self.object.tags.all()
        ).exclude(id=self.object.id).distinct()[:4]
        return context


class TaggedVideoListView(ListView):
    model = Video
    template_name = 'videos/tagged.html'
    context_object_name = 'videos'
    paginate_by = 12

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Video.objects.filter(tags=self.tag).prefetch_related('tags').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['all_tags'] = Tag.objects.all()
        return context