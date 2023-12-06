from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'routers', WonderViewSet)

urlpatterns = [
    path('', index),
    path('wonders/', WonderAPIView.as_view()),
    path('search/<slug:field_slug>/', SearchView.as_view()),
    path('wonders/<int:pk>/', WonderAPIView.as_view()),
    path('wonders/wonderlist/', WonderList.as_view()),  # generics
    path('wonders/wondercreate/', WonderCreate.as_view()),
    path('wonders/wonderretrieve/<int:pk>/', WonderRetrieve.as_view()),
    path('wonders/wonderdestroy/<int:pk>/', WonderDestroy.as_view()),
    path('wonders/wonderupdate/<int:pk>/', WonderUpdate.as_view()),
    path('wonders/wonderviewset/', WonderViewSet.as_view({'get': 'list'})),  # viewset
    path('wonders/wonderviewset/<int:pk>/', WonderViewSet.as_view({'put': 'update'})),
    path('wonders/wonderviewset/', include(router.urls)),  # routers
    path('wonders/myauth/', include('rest_framework.urls')),  # auth
]

