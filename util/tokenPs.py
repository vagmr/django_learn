"""
@文件        :tokenPs.py
@说明        :对token进行处理 
@时间        :2024/01/31 15:15:17
@作者        :vagmr
@版本        :1.1
"""


from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.conf import settings


def get_token_data(token):
    """
    从提供的令牌中获取令牌数据。
    """
    token_backend = TokenBackend(
        algorithm=settings.SIMPLE_JWT['ALGORITHM'],
        signing_key=settings.SIMPLE_JWT['SIGNING_KEY']
    )
    try:
        # 验证并解码令牌
        valid_data = token_backend.decode(token, verify=True)
        return valid_data
    except (InvalidToken, TokenError):
        print("Token is invalid or expired")
        raise InvalidToken("Token is invalid or expired")


def get_jwt_from_authorization_header(header_value):
    """
    从授权头部中提取 JWT 令牌。
    """
    auth_header_prefix = settings.SIMPLE_JWT['AUTH_HEADER_TYPES'][0].lower()
    if header_value and header_value.lower().startswith(auth_header_prefix):
        return header_value[len(auth_header_prefix) + 1:]  # 加 1 以去掉前缀后的空格
    else:
        return None
