from django import forms
from . import models

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = models.BookStroeModel
        fields = ['book_name', 'author', 'author_email', 'category', 'publish_country' ]