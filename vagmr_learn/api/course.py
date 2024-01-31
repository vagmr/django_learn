from rest_framework.response import Response
from rest_framework.decorators import api_view

from util.tokenPs import get_jwt_from_authorization_header, get_token_data
from .models import Course
from .jsonify import CourseSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        token = get_jwt_from_authorization_header(
            request.headers.get('Authorization', ''))
        if not isinstance(token, str):
            # 处理令牌不是字符串的情况
            return Response({'error': '无效的令牌类型'}, status=status.HTTP_400_BAD_REQUEST)
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        datas = get_token_data(token)
        print(datas)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        course = CourseSerializer(data=request.data, partial=True)
        if course.is_valid():
            course.save(teacher=request.user)
            return Response(course.data, status=status.HTTP_201_CREATED)
        return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(data={'msg': '课程不存在', 'code': 404, 'error': True}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
