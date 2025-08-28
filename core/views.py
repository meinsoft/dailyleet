from django.views.generic import TemplateView
from videos.models import Video
from blog.models import Post
import requests
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # --- Existing context ---
        context['featured_videos'] = Video.objects.filter(is_featured=True).order_by('-created_at')[:6]
        context['latest_posts'] = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # --- YouTube API ---
        

        # Kanal statistikası
        try:
            channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
            ch_data = requests.get(channel_url).json()
            stats = ch_data.get("items", [])[0]["statistics"]
            subscribers = int(stats.get("subscriberCount", 0))
            views = int(stats.get("viewCount", 0))
        except Exception:
            subscribers, views = 0, 0

        # Playlist video sayı (solved problems)
        solved = 0
        try:
            next_page = ""
            while True:
                pl_url = (
                    f"https://www.googleapis.com/youtube/v3/playlistItems"
                    f"?part=id&playlistId={playlist_id}&maxResults=50&key={api_key}"
                    f"{'&pageToken='+next_page if next_page else ''}"
                )
                pl_data = requests.get(pl_url).json()
                solved += len(pl_data.get("items", []))
                next_page = pl_data.get("nextPageToken")
                if not next_page:
                    break
        except Exception:
            solved = 0

        # --- Add YouTube stats to context ---
        context["subscribers"] = subscribers
        context["views"] = views
        context["solved"] = solved

        return context
