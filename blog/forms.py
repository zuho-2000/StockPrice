from django import forms

from .models import Item
from .models import Shop
from .models import Price

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('iName','genre','stock', 'under',)

class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('sName', 'area',)

class PriceForm(forms.ModelForm):

    class Meta:
        model = Price
        fields = ('item', 'shop', 'price', 'volume',)