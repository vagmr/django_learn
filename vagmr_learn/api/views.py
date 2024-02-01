"""
@文件        :views.py
@说明        :使用rest_framework 
@时间        :2024/01/31 14:23:24
@作者        :vagmr
@版本        :1.1
"""


from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from .jsonify import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, RoomSerializer, UserInfoSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .models import Room
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .permission import CustomIsAdminUser
from django.contrib.auth.models import User


class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


@api_view(['GET'])
@permission_classes((CustomIsAdminUser,))
def get_all_users(req):
    if req.method == 'GET':
        users = User.objects.all()
        serializer = UserInfoSerializer(instance=users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        if not request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': '数据不能为空'})
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    # 登录
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except (TokenError, InvalidToken) as e:
            print(e)
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data)


class CustomTokenRefreshView(TokenRefreshView):
    # 刷新token
    serializer_class = CustomTokenRefreshSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    print("jwt_response_payload_handler执行")
    if user is None:
        user = {"id": 0, "username": "default"}
    return {
        'token': token,
        # 添加需要的任何用户信息
        'user_id': user.id,
        'username': user.username,
    }
