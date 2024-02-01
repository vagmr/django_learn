from django.urls import include, path
from api.views import CustomTokenObtainPairView, CustomTokenRefreshView, RoomView, UserRegistrationView, get_all_users
from api.course import CourseList, CourseViewSet, GCourseDetail, GCourseList, course_detail, course_list
from rest_framework.routers import DefaultRouter

# 使用router
router = DefaultRouter()
router.register(prefix='course/viewsets',
                basename='course_viewsets', viewset=CourseViewSet)

app_name = 'api'
urlpatterns = [
    path("", RoomView.as_view(), name="room"),
    path("user/", get_all_users, name="users"),
    path("course/", course_list, name="course"),
    path("course/<int:pk>/", course_detail, name="detail"),
    path("courseList/", CourseList.as_view(), name="courseList"),
    path("g_list/", GCourseList.as_view(), name=""),
    path("g_course/<int:id>", GCourseDetail.as_view(), name="gcbv"),
    path("login/", CustomTokenObtainPairView.as_view(), name="jwt"),
    path('register/', UserRegistrationView.as_view(), name="register"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls))
]
# 视图集
"""  path("course/viewsets/",
         CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name="course_viewsets"),
    path("course/viewsets/<int:pk>/",
         CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), 
         name="course_viewsets"),使用视图集的方式可以实现CRUD,配合router使用 
    """
