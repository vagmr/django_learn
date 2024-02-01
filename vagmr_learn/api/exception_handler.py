"""
@文件        :exception_handler.py
@说明        :使用自定义异常处理 
@时间        :2024/01/31 20:56:47
@作者        :vagmr
@版本        :1.1
"""
import inspect
from rest_framework.views import exception_handler
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from . import exceptions


def get_custom_exceptions(module):
    """
    从给定模块中检索自定义异常。

    参数:
        module: 要从中检索自定义异常的模块。

    返回:
        在模块中找到的自定义异常列表。
    """
    custom_exceptions = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, APIException) and obj is not APIException:
            custom_exceptions.append(obj)
    return custom_exceptions


custom_exceptions_list = get_custom_exceptions(exceptions)


def custom_exception_handler(exc, context):
    """
    自定义异常处理函数，用于处理特定的异常，并为响应添加HTTP状态码。
    参数：
    - exc: 正在处理的异常。
    - context: 异常发生的上下文。
    返回：
    - Response: 带有HTTP状态码的响应对象。
    """
    # 先调用默认的异常处理函数
    response = exception_handler(exc, context)

    # 如果异常是InvalidToken或TokenError，则返回一个自定义的响应
    if isinstance(exc, (InvalidToken, TokenError)):
        custom_response_data = {
            "detail": "您的登录信息已失效，请重新登录。",
            "code": "authorization_failed",
            'author': 'vagmr',
            "messages": [
                {
                    "token_class": "AccessToken",
                    "token_type": "access",
                    "message": "Token is invalid or expired(token过期或无效)",
                    "info": "有效期：1小时"
                }
            ]
        }
        response = Response(custom_response_data,
                            status=status.HTTP_401_UNAUTHORIZED)
    # 检查异常是否在自定义异常列表中
    if any(isinstance(exc, cls) for cls in custom_exceptions_list):
        print(custom_exceptions_list)
        custom_response_data = {
            "code": exc.status_code,
            "msg": str(exc.detail),
            'author': 'vagmr',
            'mark': str(exc.default_code),
            'data': exc.data
        }
        response = Response(custom_response_data, status=exc.status_code)

    return response
