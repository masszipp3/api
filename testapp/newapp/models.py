from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name=models.CharField(max_length=10)
    email=models.CharField(max_length=90,null=True)
    password=models.CharField(max_length=10,null=True)
    phone = models.CharField(max_length=10,null=True)

class Category(models.Model):
    category_name = models.CharField(max_length=12)
    category_description = models.CharField(max_length=12) 

class Products(models.Model):
    product_name = models.CharField(max_length=12)
    product_price = models.CharField(max_length=12)
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)  
    
      


