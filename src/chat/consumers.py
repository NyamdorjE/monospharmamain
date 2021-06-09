import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from src.courses.models import Lesson

from .models import Message, Room
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Channel ашиглан хэрэглэгчийн нэг group-д оруулах хэсэг
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # group_discard ашиглан groupees гарах
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Websocket ашиглан хуудаснаас дата татах
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data, "/*****")
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        # Хүлээн авсан датаг илгээх
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )
    
    # Бусад group-д байгаа датаг хүээн авах
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        room = Lesson.objects.filter(title=room).first()
        user = User.objects.filter(username=username).first()
        print(room)
        print(user)
        Message.objects.create(username=user, lesson=room, content=message)
        