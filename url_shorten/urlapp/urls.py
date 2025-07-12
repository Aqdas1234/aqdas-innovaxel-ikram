from django.urls import path
from .views import ShortenURLView, ShortURLDetailView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten-url'),
      path('shorten/<str:shortCode>', ShortURLDetailView.as_view(), name='short-url-detail'),
]
