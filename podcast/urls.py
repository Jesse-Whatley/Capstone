from django.urls import path
from .views import podcast_list_view



urlpatterns = [
    path('podcast/', podcast_list_view, name="podcast_list"),
]
