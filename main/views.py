from django.views.generic import TemplateView, ListView
from .openweather import OpenWeather
from bs4 import BeautifulSoup
from .filters import CityFilterForm
from .models import City
from .forms import SearchForm


class IndexPageView(TemplateView):
    template_name = 'main/pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        query = self.request.GET.get('query')
        context['search_form'] = SearchForm()

        if query is not None and query != '':
            search_results = []
            open_weather = OpenWeather()
            cities_dict = open_weather.find(query)
            for record in cities_dict:
                record_id = record.get('record_id')
                City.objects.update_or_create(**record, defaults={'record_id': record_id})
                city = City.objects.filter(record_id=record_id).first()
                search_results.append(city)

            context['cities'] = search_results

            if len(search_results) == 0:
                context['error'] = 'Not found'

        return context


class ResultsPageView(ListView):
    template_name = 'main/pages/results.html'
    context_object_name = 'cities'
    model = City
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ResultsPageView, self).get_context_data()
        context['city_filter'] = CityFilterForm(data=self.request.GET)

        return context

    def get_queryset(self):
        queryset = super(ResultsPageView, self).get_queryset().order_by('pk')
        city_filter = CityFilterForm(queryset=queryset,
                                     data=self.request.GET)

        return city_filter.qs
