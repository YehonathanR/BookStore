from rest_framework import serializers

from books.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'title', 'code', 'linenos', 'language', 'style']