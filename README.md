# Connectin | Spice Assignmet

- [API Documentation](#api-documentation)

## How to run project ?

**Install redis and run it before running the project**

```shell
$ pip3 install -r requirements.txt

$ cd connectin

$ python3 manage.py makemigrations
$ python3 manage.py migrate

$ python3 manage.py runserver

```

*In another shell*
```shell
$ celery -A connectin worker -l info
```

## API Documentation


## Real time notification

It uses websocket for sending realtime notification.

WebSocket /ws/notifs/

**Authorizaion** Bearer Token

Token \<token\>

**Received message format**

```Json
{
    "type": "",
    "message": ""
}
```
**Example**
```Json
{
    "type": "notif",
    "message": "john sent you connection request!"
}
```

## User

**Register User**

POST /api/user/register/

**Authorization**

None

**Body**
```JSON
{
    "username": "",
    "full_name": "",
    "email": "",
    "contact_number": "",
    "address": "",
    "industry": "",
    "company_name": "",
    "password": ""
}
```
---
**Login User**

POST /api/user/login/

**Authorization**

None

**Body**
```JSON
{
    "username": "user2",
    "password": "SecurePass123!"
}
```
-------
**Refresh Access Token**

POST /api/token/refresh/

**Authorization**

None

**Body**
```JSON
{
    "refresh": "",
}
```
---
**Search User**

GET /api/user/search/

**Authorization** Bearer Token

Token    \<token\>

**Query Parameters**

name = 

email = 

company_name = 

number = 


## Connection

**Send Connection**

POST /api/connection/send/

**Authorization** Bearer Token

Token \<token\>

**Body**
```JSON
{
    "to_user_id":""
}
```
---

**Decide Connection Request**

POST /api/connection/decide/

**Authorization** Bearer Token

Token \<token\>

**Body**
```JSON
{
    "connection_id": "",
    "do": "" // accept | reject | cancel
}
```
*'do'* has three values
- *accept* to accept the connection by receiver
- *reject* to reject the connection by receiver
- *cancel* to cancel the connection by sender

---
**List all Connections**

GET /api/connection/accepted/

**Authorization** Bearer Token

Token \<token\>

---

**List Connection Request**

GET /api/connection/requests/

**Authorization** Bearer Token

Token \<token\>

---
**List Sent Connection Requests**

GET /api/connection/sent-requests/

**Authorization** Bearer Token

Token \<token\>

## Notification

**List Notifications**

GET /api/notification/

**Authorization** Bearer Token

Token \<token\>

---
**Delete Notificaiton**

DELETE /api/notification/:uid/

**Authorization** Bearer Token

Token \<token\>

**Path Variables**

uid - notification's id

---
**Update Notification**

PUT /api/notification/:uid/

**Authorization** Bearer Token

Token \<token\>

**Path Variables**

uid - notification's id

**Body**
```JSON
{
    "body":""
}
```

---
**Create Notification**

POST /api/notification/create/

**Authorization** Bearer Token

Token \<token\>

**Body**
```JSON
{
    "body":""
}
```
