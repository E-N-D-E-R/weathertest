from django.urls import re_path, path, include
from main.views import *

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('results', ResultsPageView.as_view(), name='results')
]