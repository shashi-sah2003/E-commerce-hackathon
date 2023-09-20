from django import forms
from . models import Product

class CreateNewProduct(forms.ModelForm):
    productName = forms.CharField(max_length = 100 , label = "Product Name")
    productDescription = forms.CharField(max_length = 550 , label='Description')
    productCost = forms.IntegerField(label='Cost in ₹')
    productImage = forms.ImageField(label='Product Image')

    def __init__(self, *args, **kwargs):
        super(CreateNewProduct, self).__init__(*args, **kwargs)
        self.fields['productDescription'].widget.attrs['id'] = 'product-desc'

    class Meta:
        model = Product
        fields = ['productName','productDescription','productCost','productImage']