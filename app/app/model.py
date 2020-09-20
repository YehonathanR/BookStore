from django.db import models


class Authors(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)



