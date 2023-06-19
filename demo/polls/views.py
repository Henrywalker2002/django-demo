from rest_framework import status
from rest_framework.decorators import action  # ,api_view
from .serlializers import BookSerializer, AuthorSerializer, UserSerializer, BookPostSerializer
from rest_framework.response import Response
from .models import Book, Author, CustomUser
from rest_framework import viewsets, permissions
# from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
# from knox.auth import AuthToken
# from django.contrib.auth.backends import ModelBackend
from django.shortcuts import get_object_or_404

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


class CustomBookViewSet(viewsets.ModelViewSet):
    def get_object(self):
        if self.action == 'viewBookByName':
            return get_object_or_404(self.get_queryset(), name=self.kwargs['pk'])
        return super().get_object()

    def get_queryset(self):
        if self.action == 'viewBookByAuthorName':
            qs = Book.objects.prefetch_related('author').all()
            return qs
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'create':
            return BookPostSerializer
        return super().get_serializer_class()

    # def get_serializer_context(self):
    #     if self.action == 'viewBookByAuthorName':
    #         context = super(CustomBookViewSet, self).get_serializer_context()
    #         return context
    #     return super().get_serializer_context()


class BookViewSet(CustomBookViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    @action(methods=['get'], detail=True)
    def viewBookByAuthorName(self, request, pk=None):
        querySet = self.get_queryset()
        instance = querySet.filter(author__name=pk).all()
        # querySet[0]['author'] = instance

        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def viewBookByName(self, request, pk=None):
        return self.retrieve(request, pk=pk)


class AuthorViewSet(viewsets.ModelViewSet):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        user = CustomUser.objects.create_user(
            request.data['email'], request.data['password'])
        return Response(user, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_name="login")
    def login(self, request):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # user = self.queryset.filter(username = serializer.data['username'])
        # if user.count():
        #     check = check_password(request.data['password'], user.get().password)
        #     if check : 0
        #         return Response(data = "True", status= status.HTTP_200_OK)
        # return Response(data = "not found", status=status.HTTP_401_UNAUTHORIZED)
        user = authenticate(
            request, username=request.data['email'], password=request.data['password'])
        if user:
            token = Token.objects.create(user=user)
            return Response({"token": token.key})
        return Response("incorrect email or password")

# class AuthorList(APIView):

#     def get(self, request, format = None):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many = True)
#         return Response(serializer.data)

# using mixin

# class AuthorList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
