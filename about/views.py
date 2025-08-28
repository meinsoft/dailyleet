from django.views.generic import TemplateView
from .models import Profile, Experience, Skill


class AboutView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['experiences'] = Experience.objects.all()
        context['skills'] = Skill.objects.all()
        context['skills_by_category'] = {
            category[0]: Skill.objects.filter(category=category[0])
            for category in Skill.CATEGORY_CHOICES
        }
        return context