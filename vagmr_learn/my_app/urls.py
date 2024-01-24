from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second, name='second'),
    path('pdf/', views.send_pdf, name='pdf'),
]
