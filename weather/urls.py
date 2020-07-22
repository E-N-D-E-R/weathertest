from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("select2/", include('django_select2.urls')),
    path('', include('main.urls')),
]
