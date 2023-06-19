from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'author', views.AuthorViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'book', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls))
]
