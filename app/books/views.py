from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from books.models import Books
from books.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

