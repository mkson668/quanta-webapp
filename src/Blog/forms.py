from django import forms 
from .models import Article

class ArticleModelForm(forms.ModelForm):
    # we can override the defined fields in Meta
    title       = forms.CharField()
    content = forms.CharField(required = False, widget = forms.Textarea(attrs={
        "placeholder": "some description",
        "class": "new-class",
        "id": "id-for-text-area",
        "row": 20,
        "col": 20,
    }))
    active = forms.BooleanField(required=False) 
    
    # using this allows us to override models fields using form type fields
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]