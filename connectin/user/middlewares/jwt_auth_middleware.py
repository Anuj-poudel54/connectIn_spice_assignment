
from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import UntypedToken
from jwt import decode as jwt_decode

from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import AnonymousUser

User = get_user_model()

@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return AnonymousUser()

class JwtAuthMiddleware:
   """ Auth middleware used in websocket for authenticating using jwt """
   
   def __init__(self, app):
        self.app = app

   async def __call__(self, scope, receive, send):

        headers = dict(scope["headers"])

        auth_header: bytes = headers.get(b"authorization")

        if not auth_header:
            scope['user'] = AnonymousUser()
            return await self.app(scope, receive, send)
        
        name, token = auth_header.decode().split(" ")
        if name.lower() != "bearer":
            raise ValueError(f"Invalid token name {name}")
        
        # Validating jwt and getting user id to get user instance
        try:
            UntypedToken(token)
            decoded_data = jwt_decode(token.encode(), settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_data['user_id']

            scope['user'] = await get_user(user_id)

        except Exception as  e:
            print("ERROR: while validating jwt token in middleware\n", e)
            scope['user'] = AnonymousUser()


        return await self.app(scope, receive, send)