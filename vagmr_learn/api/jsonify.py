"""
@文件        :jsonify.py
@说明        :序列化器 
@时间        :2024/01/31 14:23:02
@作者        :vagmr
@版本        :1.1
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Room
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        read_only_fields = ("created_at",)


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.ReadOnlyField(source="teacher.username")

    class Meta:
        model = Course
        fields = ('id', 'name', 'info', 'price',
                  'teacher', 'created_at', 'updated_at')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['type'] = 'user'
        token['author'] = 'vagmr'
        # token['custom_claim'] = 'custom_value'
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        token = data.pop('access', None)  # Remove the 'access' key
        if not token:
            raise serializers.ValidationError('无效的令牌。')
        data['access_token'] = token
        data['msg'] = '登录成功'
        # data['custom_data'] = 'value'
        data['msg'] = '登录成功'
        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    """注册的序列化器

    Args:
        serializers (_type_): _description_

    Raises:
        serializers.ValidationError: _description_
        serializers.ValidationError: _description_
        serializers.ValidationError: _description_

    Returns:
        _type_: 返回的数据
    """
    email = serializers.EmailField(error_messages={'required': '邮箱不能为空。'})
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True,
        error_messages={'password': '两次密码不一致。', 'required': '确认密码不能为空。'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6,
                         'error_messages': {'required': '密码不能为空。', 'min_length': '密码不能少于6位。'}},
            'username': {'required': True, 'min_length': 5,
                         'error_messages': {'required': '用户名不能为空。', 'min_length': '用户名不能少于5位。', 'unique': '该用户名已经被注册。'},
                         },
            'email': {
                'error_messages': {
                    'required': '邮箱不能为空。',
                }
            }
        }

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'username': '该用户名已经被注册。'})
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': '该电子邮件已经被注册。'})
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': '两次密码不一致。'})
        return attrs

    def save(self, **kwargs):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account
