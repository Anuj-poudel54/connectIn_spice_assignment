from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Notification
from .serializer import NotificationSerializer

from django.http import HttpRequest

class NotificationApiView(APIView):

    def get(self, request: HttpRequest):
        user = request.user
        all_notifs = Notification.objects.filter(user=user)
        notifs_ser = NotificationSerializer(all_notifs, many=True)

        return Response(data=notifs_ser.data, status=200)
