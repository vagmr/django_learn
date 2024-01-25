from cProfile import label
from django import forms
from my_app.models import Books
from django.forms import ModelForm, NumberInput, TextInput
from django.utils.safestring import mark_safe
from django.utils.html import escape


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
    def __init__(self, *args, **kwargs):
        super(BooksModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.label = mark_safe(
                '<span class="my-label-class">%s</span>' % escape(field.label))

    class Meta:
        model = Books
        fields = '__all__'  # ['isbn', 'title', 'author', 'pages', 'price']
        widgets = {
            'isbn': TextInput(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control'}),
            'pages': NumberInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {

        }
        error_messages = {

        }
