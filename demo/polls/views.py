from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.decorators import api_view, action
from .serlializers import BookSerializer, AuthorSerializer, UserSerializer
from rest_framework.response import Response
from .models import Book, Author, CustomUser
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, mixins, generics, permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *
from django.contrib.auth import authenticate 
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
# from knox.auth import AuthToken
from django.contrib.auth.backends import ModelBackend

# from django.contrib.auth import authenticate
# Create your views here.
# def index(request):
#     return HttpResponse("hello world")

# @api_view(['POST'])
# def add_books(request):
#     book = BookSerializer(data = request.data)
#     if book.is_valid():
#         book.save()
#         return Response(book.data)
#     else :
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def add_authors(request):
#     author = AuthorSerializer(data = request.data)
#     print(author)
#     author.is_valid(raise_exception = True)
#     author.save()
#     return Response(data = author.data)

# @api_view(['GET'])
# def get_author(request):
#     dic = request.query_params.dict()
#     if 'id' in dic.keys():
#         items = Author.objects.filter(id = dic['id'])
#     else :
#         items  = Author.objects.all()
#     serializer = AuthorSerializer(items, many = True) 
#     # serializer.is_valid(raise_exception = True)
#     return Response(data = serializer.data)

# @api_view(['PUT'])
# def update_author(request, key):
#     author = Author.objects.filter(pk = key)
#     if not author: 
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = AuthorSerializer(instance = author, data = request.data)
#     serializer.is_valid(raise_exception  = True)
#     serializer.save()
#     return Response(request.data)

# @api_view(['DELETE'])
# def delete_author(request, key):
#     author = Author.objects.filter(id = key) 
#     if not author: 
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     author.delete()
#     return Response(status= status.HTTP_200_OK)
        
# class CustomModelViewSet(viewsets.ModelViewSet):
#     def get_serializer_class(self):
#         if self.action == "login":
#             return UserSerializer
#         return UserSerializer

# class TokenAuthentication:
#     def authenticate(self, request):
        
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
    @action(methods= ['get'],detail= False, url_path="getBookByAuthor")
    def viewBookByAuthor(self, request, name = "author2"):
        qs = Book.objects.select_related('author').all()
        books = qs.filter(author__name = name)
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)

class AuthorViewSet(viewsets.ModelViewSet):
    
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# def authenticate(request, email = None, password = None):
#     user = CustomUser.objects.all().filter(email = email)
#     if user.count():
#         check = check_password(request.data['password'], user.get().password)
#         if check :
#             return user 
#     return None

class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
    def create(self, request, *args, **kwargs):
        user = CustomUser.objects.create_user(request.data['email'], request.data['password'])
        return Response(user, status=status.HTTP_201_CREATED)
    
    @action(detail= False, methods= ['post'], url_name="login")
    def login(self, request):
        
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        # user = self.queryset.filter(username = serializer.data['username'])
        # if user.count():
        #     check = check_password(request.data['password'], user.get().password)
        #     if check : 0
        #         return Response(data = "True", status= status.HTTP_200_OK)
        # return Response(data = "not found", status=status.HTTP_401_UNAUTHORIZED)
        user = authenticate(request, username = request.data['email'], password  = request.data['password'])
        if user: 
            token = Token.objects.create(user = user)
            return Response({"token" : token.key})
        return Response("incorrect email or password")

# class AuthorList(APIView):
    
#     def get(self, request, format = None):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many = True)
#         return Response(serializer.data)
    
#using mixin 

# class AuthorList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer 
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)