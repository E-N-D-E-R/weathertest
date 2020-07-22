from django.db import models


class City(models.Model):
    """ City weather record"""
    date = models.DateTimeField(blank=True, null=True, default=None)
    icon = models.TextField(blank=True, null=True, default=None)
    country = models.TextField(blank=True, null=True, default=None)
    city_name = models.TextField(blank=True, null=True, default=None)
    weather_description = models.TextField(blank=True, null=True, default=None)
    record_id = models.IntegerField(default=0)
    wind = models.IntegerField(default=0)
    clouds = models.IntegerField(default=0)
    pressure = models.IntegerField(default=0)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    temperature_from = models.FloatField(default=0)
    temperature_to = models.FloatField(default=0)

    def __str__(self):
        return '{},{}'.format(self.city_name, self.country)
