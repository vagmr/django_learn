from django.urls import path

from api.views import CustomTokenObtainPairView, RoomView, UserRegistrationView
from api.course import course_detail, course_list
app_name = 'api'
urlpatterns = [
    path("", RoomView.as_view(), name="room"),
    path("course/", course_list, name="course"),
    path("course/<int:pk>/", course_detail, name="detail"),
    path("login/", CustomTokenObtainPairView.as_view(), name="jwt"),
    path('register/', UserRegistrationView.as_view(), name="register"),
]
