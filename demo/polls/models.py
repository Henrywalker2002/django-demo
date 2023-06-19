from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Author(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField("birthday", help_text="format = '%d-%m-%Y'")

    # owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, default= 1)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    # author = models.ForeignKey(Author, on_delete = models.CASCADE)
    author = models.ManyToManyField(Author)
    year = models.IntegerField(help_text="example : 2023")

    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
