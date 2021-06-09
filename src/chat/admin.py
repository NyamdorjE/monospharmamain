from django.contrib import admin
from src.chat.models import Room, Message


# Register your models here.


admin.site.register(Room),
admin.site.register(Message)