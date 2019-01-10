import json
import urllib.request
import string


class AirQualityData:
    @staticmethod
    def give_all_stations():
        url = 'http://api.gios.gov.pl/pjp-api/rest/station/findAll'
        with urllib.request.urlopen(url) as url:
            stations_list = json.loads(url.read().decode())

        stations_dict = {}
        for station in stations_list:
            stations_dict[station['stationName']] = station['id']

        return stations_dict

    @staticmethod
    def find_stations_city(city_name: string):
        url = 'http://api.gios.gov.pl/pjp-api/rest/station/findAll'
        with urllib.request.urlopen(url) as url:
            stations_list = json.loads(url.read().decode())

        city_stations_dict = {}
        for station in stations_list:
           if station['city']['name'] == city_name:
               city_stations_dict[station['stationName']] = station['id']

        return city_stations_dict

    @staticmethod
    def give_data_id(station_id: int):
        url = 'http://api.gios.gov.pl/pjp-api/rest/station/sensors/{}'
        url_getData = 'http://api.gios.gov.pl/pjp-api/rest/data/getData/{}'
        air_data = {}

        with urllib.request.urlopen(url.format(station_id)) as url:
            sensors_data = json.loads(url.read().decode())

        for sensor in sensors_data:
            with urllib.request.urlopen(url_getData.format(sensor['id'])) as url:
                param_data = json.loads(url.read().decode())
            air_data[sensor['param']['paramCode']] = param_data['values']

        return air_data
