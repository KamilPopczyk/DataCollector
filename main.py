from AirQualityData import *
import string
import csv
import time
import datetime


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


def add_data_to_csv(file_name: string, data_dict):
    if file_name.find('.csv') == -1:
        file_name += '.csv'
    group_keys = list(data_dict.keys())

    with open(file_name, newline='', mode='r+') as csvfile:
        date_list = []
        reader = csv.DictReader(csvfile)
        for row in reader:
           date_list.append(row['Date'])
        last_date = date_list[-1]
        date_list.clear()

        data_writer = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)

        new_data = []

        for i in range(len(data_dict[group_keys[0]])):      # find index of last date
            if last_date == data_dict[group_keys[0]][i]['date']: # tutaj cos poprawic  sprawdzic czy pozniejsza data
                break
            else:   # add new data
                data_list = []
                data_list.append(data_dict[group_keys[0]][i]['date'])
                for group in group_keys:
                    data_list.append(data_dict[group][i]['value'])
                new_data.append(data_list)

        # add new data to csv file
        new_data = reversed(new_data)
        for data in new_data:
            data_writer.writerow(data)





if __name__ == "__main__":
    AirQualityData.give_all_stations()
    wroc_stations = AirQualityData.find_stations_city('Wrocław')

    print("Start date data collecting: ", datetime.datetime.now())
    for station in wroc_stations:
        air_data = AirQualityData.give_data_id(wroc_stations[station])
        save_data_csv(station, air_data)

    while True:
        time.sleep(120*60)   # every 2h check new data
        print("New data added: ", datetime.datetime.now())
        for station in wroc_stations:
            air_data = AirQualityData.give_data_id(wroc_stations[station])
            add_data_to_csv(station, air_data)
