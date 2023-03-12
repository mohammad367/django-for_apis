from django.urls import path, include
from .views import BookListiew

url_patterns=[
    path('',BookListiew.as_view(),name='home')
]