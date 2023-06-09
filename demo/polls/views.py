from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from .serlializers import BookSerializer, AuthorSerializer
from rest_framework.response import Response
from .models import Book, Author
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, mixins, generics
from rest_framework.views import APIView

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

class AuthorViewSet(viewsets.ModelViewSet):
    
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


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