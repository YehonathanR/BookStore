from django.db import models
from django.db.models import Q


class Authors(models.Model):
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
