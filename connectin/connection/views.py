from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from .serializer import ConnectionSerializer, ConnectionListSerializer
from .models import Connection
from notification.models import Notification

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ConnectionApiView(ViewSet):

    def send_connection(self, request: Request):
        data = {"from_user": request.user.pk}
        req_data = request.data
        to_user_id = req_data.get("to_user_id")

        to_user = UserModel.objects.filter(uid=to_user_id)
        if not to_user.exists():
            return Response(data={"detail": "User not found!"}, status=404)

        data['to_user'] = to_user_id
        connection_ser = ConnectionSerializer(data=data)

        if connection_ser.is_valid():
            connection_ser.save()
            message = f"You sent connection request to {to_user.first().username}!"
            
            Notification.objects.create(body=message, user=request.user)

            # Creating and sending notification to connection request receiver
            notification = Notification(body=f"{request.user.username} sent you connection request!", user=to_user.first())
            notification.save()
            notification.notify_user()
            
            return Response(data={"detail": message}, status=200)

        return Response(data=connection_ser.errors, status=422)
    
    def decide_connection(self, request: Request):
        """ Accpet, Reject or Cancel the connection request """

        req_data = request.data
        connection_id = req_data.get("connection_id")

        if not connection_id:
            return Response(data={"detail": "Please provide connection id!"}, status=404)
        
        try:
            connection_request = Connection.objects.get(uid=connection_id)
        except:
            return Response(data={"detail": "Connection request not found!"}, status=404)
        
        choice = req_data.get("do")
        if not choice.strip() and choice not in {'accept', 'reject', 'cancel'}:
            return Response(data={"detail": "Only accept, reject or cancel is allowed!"}, status=404)


        if connection_request.from_user == request.user and choice == "cancel":
            # Only user who sent connection can cancel it
            connection_request.delete()
            return Response(data={"detail": "Connection request canceled!"}, status=200)


        # Only user who receives connection can accept or reject it
        if connection_request.to_user == request.user:
            if choice == "accept":
                connection_request.accepted = True
                connection_request.save()
                
                notif = Notification.objects.create( body=f"{connection_request.to_user.username} accepted your connection request!", user=connection_request.from_user)
                notif.notify_user()
                return Response(data={"detail": "Connection request Accepted!"}, status=200)

            elif choice == "reject" and not connection_request.accepted:
                connection_request.delete()
                
                notif = Notification.objects.create( body=f"{connection_request.to_user.username} rejected your connection request!", user=connection_request.from_user)
                notif.notify_user()
                return Response(data={"detail": "Connection request rejected!"}, status=200)
            
        return Response(data={"detail": f"You are not authorized to perform this request!"}, status=401)

    def list_request(self, request: Request):

        user = request.user
        if not user.is_authenticated or user.is_anonymous:
            return Response(data={"detail": "User does not exist!"}, status=404)

        received_requests = user.received_requests.all()
        data = ConnectionListSerializer(received_requests, many=True).data
        return Response(data=data, status=200)
    
    def list_sent_request(self, request: Request):

        user = request.user
        if not user.is_authenticated or user.is_anonymous:
            return Response(data={"detail": "User does not exist!"}, status=404)

        sent_requests = user.sent_requests.all()
        data = ConnectionListSerializer(sent_requests, many=True).data
        return Response(data=data, status=200)
