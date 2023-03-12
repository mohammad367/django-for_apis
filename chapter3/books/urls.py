from django.urls import path, include
from .views import BookListview

url_patterns=[
    path('',BookListview.as_view(),name='home')
]