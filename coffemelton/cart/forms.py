from django.contrib.auth.forms import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i))
                            for i in range(1, 11)
                            ]


class CartAddProductForm(forms.Form):
    class Meta:
        fields = ["quantity", "update"]

    quantity = forms.TypedChoiceField(
        label='Kogus',
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    update = forms.BooleanField(
        label='Uuenda',
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
