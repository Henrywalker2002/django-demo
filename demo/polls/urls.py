from django.urls import re_path,path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'author', views.AuthorViewSet)


urlpatterns = [
    path('', include(router.urls))
]