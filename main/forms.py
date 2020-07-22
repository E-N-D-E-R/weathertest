from django import forms
from .models import City
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class SearchForm(forms.Form):
    query = forms.ChoiceField(choices=[(str(city), str(city)) for city in City.objects.all()],
                              required=False)
