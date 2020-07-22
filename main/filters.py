from django_filters import FilterSet, DateFilter, CharFilter
from .models import City
from django import forms


class CityFilterForm(FilterSet):
    date_from = DateFilter(field_name='date',
                           lookup_expr='gte',
                           widget=forms.DateInput(attrs={'class': 'datepicker'}),
                           label='Date from',
                           )

    date_to = DateFilter(field_name='date',
                         lookup_expr='lte',
                         widget=forms.DateInput(attrs={'class': 'datepicker'}),
                         label='Date to')

    city_name = CharFilter(field_name='city_name',
                           lookup_expr='icontains',
                           label='City name')

    class Meta:
        model = City

        fields = {'city_name'}