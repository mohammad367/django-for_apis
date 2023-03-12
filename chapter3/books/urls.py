from django.urls import path, include
from .views import BookListview

urlpatterns=[
    path('',BookListview.as_view(),name='home')
]