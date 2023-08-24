# shop/views.py

from .models import Category, Subcategory, Product
from django.shortcuts import render

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def products_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    subcategories = category.subcategory_set.all()
    products = Product.objects.filter(subcategory__category=category)

    context = {
        'category': category,
        'subcategories': subcategories,
        'products': products,
    }

    return render(request, 'products_by_category.html', context)


def products_by_subcategory(request, subcategory_id):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.get(pk=subcategory_id)
    products = Product.objects.filter(subcategory=subcategory)

    context = {
        'categories': categories,
        'subcategory': subcategory,
        'products': products,
    }

    return render(request, 'products_by_subcategory.html', context)


def product_detail(request, slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=slug)

    context = {
        'categories': categories,
        'product': product,
    }

    return render(request, 'product_detail.html', context)
