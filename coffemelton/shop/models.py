from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('K', 'Kohv'),
    ('T', 'Tee'),
    ('V', 'Vein'),
    ('G', 'Gurmee'),
)

SUBCATEGORY_CHOICES = (
    ('oa', 'Oakohv'),
    ('jahv', 'Jahvatatud kohv'),
)


# class Category(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
#
# class Subcategory(models.Model):
#     name = models.CharField(max_length=30)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='K')
    subcategory = models.CharField(choices=SUBCATEGORY_CHOICES, max_length=4, default='A')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=50, unique=True)
    weight = models.CharField(max_length=10, default=0)
    # image = models.ImageField()

    def __str__(self):
        return self.name
