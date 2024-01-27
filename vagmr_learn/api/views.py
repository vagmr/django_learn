from rest_framework.generics import CreateAPIView, ListAPIView

from .jsonify import RoomSerializer

from .models import Room
# Create your views here.


class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token
    }
