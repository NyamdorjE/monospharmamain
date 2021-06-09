from django.urls import path

from .views import RoomView, room

urlpatterns = [
    path('', RoomView.as_view(), name='index'),
    path('<str:room_name>/<int:username>', room, name='room'),
]