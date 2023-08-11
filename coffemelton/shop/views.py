from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


def home(request):
    return render(request, 'home.html')


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = 'products'
    paginate_by = 12

    # def get_queryset(self):
    #     # You can filter products based on categories and subcategories here
    #     return Product.objects.all()
