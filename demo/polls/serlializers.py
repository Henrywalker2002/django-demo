from django.db.models import fields
from rest_framework import serializers
from .models import Book, Author
from datetime import datetime
from django.contrib.auth.models import User

from rest_framework.schemas.coreapi import AutoSchema

class BookSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Book 
        fields = ('name', 'author', 'year')
    
class AuthorSerializer(serializers.ModelSerializer):
    # input ddmmyyyy 
    name = serializers.CharField(required=True)
    birthday = serializers.DateField(required=True, input_formats = ["%d-%m-%Y"], format = '%d-%m-%Y')
    
    class Meta: 
        model = Author 
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many = True, queryset = Author.objects.all())
    
    class Meta:
        model = User 
        fields = ['id', 'username', 'authors']