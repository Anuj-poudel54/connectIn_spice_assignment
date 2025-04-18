
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserCreate

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = ([
    path('register/', UserCreate.as_view(), name='register-user'),
    path('', include(router.urls)),
])

