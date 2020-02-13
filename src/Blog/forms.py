from django import forms 
from .models import Article

class RawArticleForm(forms.Form):
    title = forms.CharField(max_length=120)
    content = forms.CharField(required=False, widget = forms.Textarea(attrs={
        "placeholder": "some description",
        "class": "new-class",
        "id": "id-for-text-area",
        "row": 20,
        "col": 20,
    }))
    active = forms.BooleanField(required=False)

