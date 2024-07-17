from django import forms
from apps.core.constants import BOOK_CATEGORY

class PostBookForm(forms.Form):
    isbn = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "isbn-input",
                "placeholder": "Enter isbn"
            }
        )
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder": "Enter text"
            }
        )
    )
    pages = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "pages-input",
                "placeholder": "Enter pages"
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "description-input",
                "placeholder": "Enter description"
            }
        )
    )
    categories = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs = {
                'class': 'form-cat'
            }
        ),
        choices=BOOK_CATEGORY
    )