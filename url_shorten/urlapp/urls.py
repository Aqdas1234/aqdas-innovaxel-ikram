from django.urls import path
from .views import ShortenURLView, ShortURLDetailUpdateDeleteView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten-url'),
    #path('shorten/<str:shortCode>', ShortURLDetailView.as_view(), name='short-url-detail'),
    #path('shorten/<str:shortCode>', ShortURLUpdateView.as_view(), name='short-url-update'),
    #path('shorten/<str:shortCode>', ShortURLDeleteView.as_view(), name='short-url-delete'),
    path('shorten/<str:shortCode>', ShortURLDetailUpdateDeleteView.as_view(), name='shorten-detail-update-delete'),

]
