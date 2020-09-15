from django.db import models

class ProductModel(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()
