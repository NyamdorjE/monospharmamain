from django.shortcuts import render
from django.views.generic import ListView

from .models import Message, Room
from django.contrib.auth.models import User


class RoomView(ListView):
    queryset = Room.objects.all()
    template_name = "chat/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room"] = Room.objects.all()
        return context


def room(request, room_name, username):
    room = Room.objects.filter(name=room_name).first()
    username = User.objects.filter(id=username).first()
    messages = Message.objects.filter(lesson=room)[0:25]

    return render(
        request,
        "chat/room.html",
        {"room_name": room_name, "name": username, "messages": messages},
    )
