from django import forms
from my_app.models import Books
from django.forms import ModelForm


class BooksForm(forms.Form):
    isbn = forms.CharField(label="ISBN", max_length=30, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label="Title", max_length=100, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label="Author", max_length=100, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    pages = forms.IntegerField(label="Pages", min_value=1, required=True,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(label="Price", required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control'}))


# 模型表单
class BooksModelForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'  # ['isbn', 'title', 'author', 'pages', 'price']
