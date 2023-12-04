from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('wonders/', WonderAPIView.as_view()),
    path('search/<slug:field_slug>/', SearchView.as_view()),
    path('wonders/<int:pk>/', WonderAPIView.as_view())
]
