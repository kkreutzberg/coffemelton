from django.contrib import admin
from django import forms
from .models import Category, Subcategory, Product


class ProductForm(forms.ModelForm):
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all())  # Add this line for subcategory selection

    class Meta:
        model = Product
        fields = ('product_name', 'subcategory', 'description', 'price', 'slug', 'weight', 'image')


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('product_name', 'subcategory', 'price')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subcategory':
            category_id = request.GET.get('category_id')
            if category_id:
                kwargs['queryset'] = Subcategory.objects.filter(category_id=category_id)
            else:
                kwargs['queryset'] = Subcategory.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        category_id = request.GET.get('category_id')
        if category_id:
            queryset |= self.model.objects.filter(subcategory__category_id=category_id)
        return queryset, use_distinct


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product, ProductAdmin)
