# Create your models here.
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30, default='tootekategooria', unique=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

    def get_subcategories(self):
        return Subcategory.objects.filter(category=self)


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=30, default='alamkategooria', unique=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.subcategory_name


# which are mandatory fields (null=...); hinnale vaja juurde saada euromärk ette?
class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    slug = models.SlugField(max_length=50, unique=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='default.png', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name


# mõtleme jooksvalt, mis tegelikult on vaja:
class Order(models.Model):
    pass


class OrderItem(models.Model):
    pass
