from django.db import models
from product.models import Product

# Create your models here.

class Cart(models.Model):
    product_id = models.IntegerField(name="product_id")
    customer_id = models.IntegerField(name="customer_id")
    qty = models.IntegerField(name="qty")
    created_at = models.DateTimeField(name="created_at")

