from rest_framework.generics import CreateAPIView, ListAPIView

from .jsonify import RoomSerializer

from .models import Room
# Create your views here.


class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
