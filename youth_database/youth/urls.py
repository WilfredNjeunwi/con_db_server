from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YouthViewSet

router = DefaultRouter()
router.register(r'youth', YouthViewSet)

urlpatterns = [
    path('', include(router.urls)),
]