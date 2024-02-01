"""
@文件        :exceptions.py
@说明        :自定义异常 
@时间        :2024/02/01 15:02:04
@作者        :vagmr
@版本        :1.1
"""
from rest_framework.exceptions import APIException
from rest_framework import status


class CourseNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = '课程不存在'
    default_code = 'course_not_found'
    data = None
