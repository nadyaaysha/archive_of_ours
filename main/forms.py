from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "title", "amount", "description", "word_Count", "genre", "character_Source"]
        