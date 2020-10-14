from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255, default='SOME STRING')
    date = models.DateTimeField('date_published')
    amount = models.BigIntegerField('amount')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)