from AirQualityData import *
import string
import csv

def save_data_csv(file_name: string, data_dict):
    if file_name.find('.csv') == -1:
        file_name += '.csv'

    group_keys = list(data_dict.keys())

    with open(file_name, 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['Date'] + group_keys)
        for i in reversed(range(len(data_dict[group_keys[0]]))):    # old first
            data_list = []
            data_list.append(data_dict[group_keys[0]][i]['date'])
            for group in group_keys:
                data_list.append(data_dict[group][i]['value'])
            data_writer.writerow(data_list)
            data_list.clear()


if __name__ == "__main__":
    AirQualityData.give_all_stations()
    wroc_stations = AirQualityData.find_stations_city('Wrocław')

    for station in wroc_stations:
        air_data = AirQualityData.give_data_id(wroc_stations[station])

        # print("Station name: ", station)
        # print(air_data['NO2'])

        save_data_csv(station, air_data)

        # for data in air_data['NO2']:
        #     print(data['value'])