from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('products/subcategory/<int:subcategory_id>/', views.products_by_subcategory, name='products_by_subcategory'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail')
]
