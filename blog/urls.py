from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",views.index, name='index'),
    path('imschool1/', views.imschool1, name='imschool1'),
    path('imschool2/', views.imschool2, name='imschool2'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('news/', views.news, name='news'),
    path('post/', views.post, name='post'),
]
