from django import forms

from .models import Item
from .models import Shop
from .models import Price

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('iName','genre','stock',)

class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('sName', 'area',)