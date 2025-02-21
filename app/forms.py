from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('category', 'title', 'model', 'description', 'price', 'engine_capacity', 'year', 'odometer', 'color', 'image')