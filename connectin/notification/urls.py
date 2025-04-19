
from django.urls import path

from .views import NotificationApiView


urlpatterns = ([
    path('', NotificationApiView.as_view(), name='notifications'),
])

