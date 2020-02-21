from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("Product Name",max_length=255)
    description = models.CharField("Description",max_length=500)
    category = models.CharField("Category Name",max_length=50,default="")
    image = models.ImageField(upload_to ="images/", default=None)
    created_at = models.DateTimeField("Created Date") 
    price = models.CharField("Price",max_length=255,default=0)