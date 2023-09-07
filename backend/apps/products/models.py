from django.db import models
from apps.users.models import User
from cloudinary.models import CloudinaryField
from apps.categories.models import Category
# Create your models here.


class Product(models.Model):
    class Meta(object):
        db_table = 'product'

    name = models.CharField(
    'Name',blank = False, null = False, max_length=200
    )

    description = models.CharField(
    'Description', blank = False, null = False, max_length=200
    )

    price = models.FloatField(
    'Price', blank=False, null=False
    )

    image = CloudinaryField(
    'Product image', blank=False, null=True
    )

    type = models.CharField(
    'Type', blank=False, null=False, max_length=800 
    )

    category = models.ForeignKey(
    Category, related_name='related_category', on_delete=models.CASCADE
    )