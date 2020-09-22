from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(first_name__isnull=False, second_name__isnull=False) | Q(company_name__isnull=False),
                name='authors_check_not_empty'),
            models.UniqueConstraint(fields=['first_name', 'second_name'], name='authors_ind_1',
                                    condition=Q(company_name__isnull=True)),
            models.UniqueConstraint(fields=['company_name'], name='authors_ind_2',
                                    condition=Q(company_name__isnull=False))

        ]


class Publisher(models.Model):
    name = models.CharField(max_length=100)


def validate_publication_date(value):
    if value > datetime.utcnow():
        raise ValidationError("publication_date cant be in the future")


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=100, null=False)
    publication_date = models.DateField(validators=[validate_publication_date])
    edition = models.IntegerField()
    available_quantity = models.IntegerField(null=False, default=0, validators=[MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(0)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


