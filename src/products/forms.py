from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    # we can override the defined fields in Meta
    title       = forms.CharField()
    description = forms.CharField(required = False, widget = forms.Textarea(attrs={
        "placeholder": "some description",
        "class": "new-class",
        "id": "id-for-text-area",
        "row": 20,
        "col": 20,
    }))
    email       = forms.EmailField()
    price       = forms.DecimalField(initial = 19.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'email',
            'price',
        ]
    
    def clean_title(self, *args, **kwargs):
        # this gets default title and cleans it
        title = self.cleaned_data.get("title")
        if not 'QUANTA' in title:
            raise forms.ValidationError("this is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("this is not a valid title")
        return email


class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField(required = False, widget = forms.Textarea(attrs={
        "placeholder": "some description",
        "class": "new-class",
        "id": "id-for-text-area",
        "row": 20,
        "col": 20,
    }))
    price       = forms.DecimalField(initial = 19.99)
