from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from books.models import Author


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
