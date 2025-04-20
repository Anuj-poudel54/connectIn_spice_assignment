from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import NotificationApiView

router = DefaultRouter()
router.register('', NotificationApiView)

urlpatterns = ([
    path('', NotificationApiView.as_view({"get": "list"}), name='list-notifications'),
    path('create/', NotificationApiView.as_view({"post": "create"}), name='create-notifications'),
])

