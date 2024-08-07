from django.shortcuts import render
from .models import Podcast

# Create your views here.


def podcast_list_view(request):
    podcasts = Podcast.objects.all()
    return render(request, 'podcast/podcast_list.html', {
        'podcasts' : podcasts
    })