# Create your models here.
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30, default='tootekategooria', unique=True)

    def __str__(self):
        return self.category_name

    def get_subcategories(self):
        return Subcategory.objects.filter(category=self)


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=30, default='alamkategooria', unique=True)

    def __str__(self):
        return self.subcategory_name


# which are mandatory fields (null=...); hinnale vaja juurde saada euromärk ette?
class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=50, unique=True)
    weight = models.CharField(max_length=6)
    image = models.ImageField(upload_to='images/', default='default.png')

    def __str__(self):
        return self.product_name


# mõtleme jooksvalt, mis tegelikult on vaja:
class Order(models.Model):
    pass


class OrderItem(models.Model):
    pass