from django import forms

from .models import Routines, Books


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Routines
        fields = ('routine_uploader_name', 'routine_description', 'document_routine',)


class BookDocumentForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('books_uploader_name', 'books_description', 'books_document',)
