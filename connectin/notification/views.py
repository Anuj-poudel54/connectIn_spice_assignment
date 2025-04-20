from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request

from .models import Notification
from .serializer import NotificationSerializer


class NotificationApiView(ModelViewSet):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request: Request, *args, **kwargs):

        request.data['user'] = request.user.uid

        return super().create(request, *args, **kwargs)

    def list(self, request: Request, *args, **kwargs):
        user = request.user
        self.queryset = self.get_queryset().filter(user=user)
        return super().list(request, *args, **kwargs)
        
        