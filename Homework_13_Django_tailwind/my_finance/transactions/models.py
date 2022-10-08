from django.db import models
from django.utils.timezone import now
from django.conf import settings


class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now)
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='income',
        null=True
    )

    def __str__(self):
        return self.description, self.id  # noQA


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now)
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='expense',
        null=True
    )

    def __str__(self):
        return self.description, self.id  # noQA


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name, self.id  # noQA