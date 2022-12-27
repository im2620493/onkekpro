from django.urls import path

from .views import Main

urlpatterns = [
    path('', Main.as_view(), name='index'),
]