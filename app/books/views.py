from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from books.models import Author, Publisher, Book
from books.serializers import AuthorSerializer, BookSerializer, PublisherSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
