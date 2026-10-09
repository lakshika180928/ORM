from django.db import models
from django.contrib import admin
class Product(models.Model):
    Product_ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Brand = models.CharField(max_length=30)
    Discount = models.FloatField()
class ProductAdmin(admin.ModelAdmin):
    list_display = ["Product_ID","Name","Category","Price","Quantity","Brand","Discount"]

 