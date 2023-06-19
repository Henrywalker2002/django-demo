from django.db.models import fields
from rest_framework import serializers
from .models import Book, Author, CustomUser
import re


class AuthorSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    birthday = serializers.DateField(required=True, input_formats=[
                                     "%d-%m-%Y"], format='%d-%m-%Y', help_text="format is '%d-%m-%Y'")

    class Meta:
        model = Author
        fields = '__all__'


class CustomModelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        """
        Custom response format.
        """
        ret = super().to_representation(instance)
        ret['Name'] = ret.pop('name')
        return ret


class BookPostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)
    year = serializers.IntegerField(required=True)

    def validate_year(self, data):
        """
        validate year : 4 number
        """
        pattern = re.compile("^\w{4}$")

        if not re.match(pattern, str(data)):
            raise serializers.ValidationError(
                "year must between 1000 and 9999")

        return data

    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(CustomModelSerializer):

    name = serializers.CharField(max_length=255, required=True)
    year = serializers.IntegerField(required=True)
    author = serializers.ListSerializer(child=AuthorSerializer())

    class Meta:
        model = Book
        fields = ['name', 'year', 'author']


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, max_length=255, style={
                                     "input_type": "password"})

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
