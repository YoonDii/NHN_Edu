from django.urls import path
from blog import views

urlpatterns = [
    path("",view=index, name='index')
]
