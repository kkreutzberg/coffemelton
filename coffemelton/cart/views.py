from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Category

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(product=product,
                 quantity=cleaned_data['quantity'],
                 update_quantity=cleaned_data['update'],
                 )
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


# def cart_update(request):
#     cart = Cart(request)
#
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('product_id'))
#         product_quantity = int(request.POST.get('product_quantity'))
#
#         cart.update(product=product_id, quantity=product_quantity)
#
#         return render(request, 'cart/cart_detail.html', {'cart': cart})

def cart_update(request):
    cart = Cart(request)

    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))  # Parse the product_id as an integer
        product_quantity = int(request.POST.get('product_quantity'))  # Parse the quantity as an integer

        # Fetch the Product object corresponding to the product_id
        product = get_object_or_404(Product, id=product_id)

        cart.update(product=product, quantity=product_quantity)  # Pass the Product object and quantity

    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    categories = Category.objects.all()

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True}
        )

    total = cart.get_total()

    return render(request, 'cart/cart_detail.html', {'cart': cart, 'total': total, 'categories': categories})
