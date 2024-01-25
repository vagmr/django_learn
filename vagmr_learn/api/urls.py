from django.urls import path

from api.views import RoomView
app_name = 'api'
urlpatterns = [
    path("", RoomView.as_view(), name="room")
]
