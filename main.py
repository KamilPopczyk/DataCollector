from AirQualityData import *


if __name__ == "__main__":
    AirQualityData.give_all_stations()
    wroc_stations = AirQualityData.find_stations_city('Wrocław')

    for station in wroc_stations:
        air_data = AirQualityData.give_data_id(wroc_stations[station])

        print("Station name: ", station)
        print(air_data)