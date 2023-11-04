from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Order, ItemCategory


class OrderAdminForm(ModelForm):
    # extra_field_1 = forms.URLField(required=False)
    # cat = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    # item
    # order
    # supplier
    # quantity
    # product_link
    test = forms.URLField(required=False)


    class Meta:
        model = Order
        fields = ('status',)
