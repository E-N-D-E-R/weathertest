from datetime import datetime as dt
import requests
import json
import pytz
import re


class OpenWeather:
    main_url = 'https://openweathermap.org/find'
    api_url = 'https://openweathermap.org/data/2.5/find'

    def parse_api_key(self):
        """ Parse search page to get current api key """
        try:
            resp = requests.get(url=self.main_url)
            if resp.status_code != 200:
                return None

            app_id = re.search(r'&appid=(.*?)";', resp.text).group(1)

            return app_id

        except Exception:
            return None

    def find(self, query):
        """ Perform search for cities via openweather api"""
        app_id = self.parse_api_key()
        results = []

        if app_id is None:
            return ''

        params = {
            'q': query,
            'type': 'like',
            'sort': 'population',
            'cnt': '30',
            'appid': app_id
        }

        try:
            resp = requests.get(url=self.api_url, params=params)

            if resp.status_code != 200:
                return None

            data = json.loads(resp.text)

            for el in data.get('list'):
                record = self.parse_to_dict(el=el)
                if record is not None:
                    results.append(record)

            return results

        except Exception:
            return None

    def parse_to_dict(self, el):
        """ Convert json data to usable format """
        try:
            record_id = el.get('id')
            city_name = el.get('name')
            weather_description = el.get('weather')[0].get('description')
            icon = el.get('weather')[0].get('icon')
            temperature = el.get('main').get('temp') - 273.15
            temperature_from = el.get('main').get('temp_min') - 273.15
            temperature_to = el.get('main').get('temp_max') - 273.15
            pressure = el.get('main').get('pressure')
            lat = el.get('coord').get('lat')
            lon = el.get('coord').get('lon')
            country = el.get('sys').get('country')
            timestamp = el.get('dt')
            datetime = dt.fromtimestamp(timestamp)
            datetime = datetime.replace(tzinfo=pytz.timezone('Europe/Kiev'))
            wind = el.get('wind').get('speed')

            dict = {
                'record_id': record_id,
                'city_name': city_name,
                'weather_description': weather_description,
                'icon': icon,
                'temperature': temperature,
                'temperature_from': temperature_from,
                'temperature_to': temperature_to,
                'pressure': pressure,
                'lat': lat,
                'lon': lon,
                'country': country,
                'date': datetime,
                'wind': wind
            }

            return dict

        except Exception:
            return None

