from django.db.models import fields
from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Book 
        fields = ('name', 'author', 'year')
    
class AuthorSerializer(serializers.ModelSerializer):
    # input ddmmyyyy 
    name = serializers.CharField(required=True)
    birthday = serializers.DateField(required=True, input_formats = ["%d-%m-%Y"])
    
    class Meta: 
        model = Author 
        fields = ('name', 'birthday')
