from django.test import TestCase, Client
from .models import Category, Subcategory, Product
from django.urls import reverse


# Create your tests here.
# To run the test: python manage.py test products
class ModelsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name='Test Category')
        self.subcategory = Subcategory.objects.create(
            category=self.category, subcategory_name='Test Subcategory'
        )
        self.product = Product.objects.create(
            subcategory=self.subcategory,
            product_name='Test Product',
            price=10.99,
            slug='test-product',
        )

    def test_category_creation(self):
        self.assertEqual(str(self.category), 'Test Category')
        self.assertEqual(self.category.get_subcategories().count(), 1)

    def test_subcategory_creation(self):
        self.assertEqual(str(self.subcategory), 'Test Subcategory')

    def test_product_creation(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_relationships(self):
        self.assertEqual(self.product.subcategory, self.subcategory)

    def test_product_price_format(self):
        self.assertEqual(str(self.product.price), '10.99')


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(category_name='Test Category')

    def test_home_view(self):
        response = self.client.get(reverse('shop:home'))  # Use 'shop:home' instead of 'home'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_category_list_view(self):
        response = self.client.get(reverse('shop:products_by_category',
                                           kwargs={'category_id': self.category.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_by_category.html')
        self.assertContains(response, 'Test Category')
