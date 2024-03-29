from django.forms import ModelForm
from cms.models import Book, Impression


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page', )


class ImpressionForm(ModelForm):
    class Meta:
        model = Impression
        fields = ('comment', )