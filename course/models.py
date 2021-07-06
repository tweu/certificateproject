from django.db import models
from django.db.models.deletion import PROTECT
from django.urls import reverse

# Create your models here.

class Brand (models.Model):
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name




class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.CharField(max_length=300, default= 'Введите описание')
    photo = models.ImageField()
    brand = models.ForeignKey(Brand, on_delete=PROTECT, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs ={'product_id': self.pk})
