
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserCreateView, UserLoginView

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = ([
    path('register/', UserCreateView.as_view(), name='register-user'),
    path('login/', UserLoginView.as_view(), name='login-user'),
    path('', include(router.urls)),
])

