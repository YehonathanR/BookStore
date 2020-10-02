from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models


def validate_publication_date(value):
    if value > datetime.utcnow():
        raise ValidationError("publication_date cant be in the future")


class Books(models.Model):
    isbn = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=100, null=False)
    publication_date = models.DateField(validators=[validate_publication_date])
    authors = models.CharField(max_length=100, null=False)
    language_code = models.CharField(max_length=100, null=False)
    num_pages = models.IntegerField()
    publisher = models.CharField(max_length=100, null=False)

