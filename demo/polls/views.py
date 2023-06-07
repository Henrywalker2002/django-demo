from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from .serlializers import BookSerializer, AuthorSerializer
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse("hello world")

@api_view(['POST'])
def add_books(request):
    book = BookSerializer(request.data)
    if book.is_valid():
        book.save()
        return Response(book.data)
    else :
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_authors(request):
    author = AuthorSerializer(data = request.data)
    print(author)
    author.is_valid(raise_exception = True)
    author.save()
    return Response(data = author.data)