from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from util.tokenPs import get_jwt_from_authorization_header, get_token_data
from rest_framework import generics

from .permission import IsOnlyOwner
from .exceptions import CourseNotFound
from .models import Course
from .jsonify import CourseSerializer
from rest_framework import status

"1.函数视图"


# from rest_framework.decorators import authentication_classes
# from rest_framework.authentication import SessionAuthentication,BasicAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication,JWTStatelessUserAuthentication
@api_view(['GET', 'POST'])
# 函数使用装饰器 @authentication_classes((JWTAuthentication,))
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


"cbv 类视图"


class CourseList(APIView):
    # 类的自定义认证 authentication_classes = []
    def get(self, req):
        """get请求

        Args:
            req (_type_): 请求

        Raises:
            CourseNotFound: 课程不存在

        Returns:
            Response: 响应
        """
        # 获取查询参数
        params = req.query_params
        queryset = None
        if params.get('id', None):
            queryset = Course.objects.filter(pk=params.get('id')).first()
        else:
            queryset = Course.objects.first()
        s = CourseSerializer(instance=queryset)
        if not queryset:
            raise CourseNotFound()
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, req):
        pass

    def put(self, req):
        pass

    def delete(self, req):
        pass


"3.通用类视图 gcbv"


class GCourseList(generics.ListCreateAPIView):
    """get 和 post 请求"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class GCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOnlyOwner]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'


"4.视图集"


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
