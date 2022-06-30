from django.db import models
class Customer(models.Model):
  name = models.CharField(max_length=200)
  phone_number = models.CharField(max_length=200)