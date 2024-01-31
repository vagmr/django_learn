"""
URL配置为vagmr_learn项目。
urlpatterns列表将URL路由到视图。有关更多信息，请参见：https://docs.djangoproject.com/en/4.2/topics/http/urls/
示例：
函数视图
1. 添加导入：从my_app导入视图
2. 将URL添加到urlpatterns：path('', views.home, name='home')
基于类的视图
1. 添加导入：从other_app.views导入Home
2. 将URL添加到urlpatterns：path('', Home.as_view(), name='home')
包括另一个URLconf
1. 导入include()函数：从django.urls导入include、path
2. 将URL添加到urlpatterns：path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("my_app/", include("my_app.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path('api-auth/', include('rest_framework.urls')),
]

handler404 = views.custom_not_found_view
