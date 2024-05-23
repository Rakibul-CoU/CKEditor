from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Book, YourModel


class YourModelForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model = YourModel
        fields = '__all__'




class BookCKEditorForm(forms.ModelForm):
    detail = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Book
        fields = '__all__'
