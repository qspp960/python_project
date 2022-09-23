
# with open("./weather_data.csv") as weather_data:

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    day = []
    condition = []
    for i,row in enumerate(data):
        if i != 0:
            day.append(row[0])
            temperature.append(int(row[1]))
            condition.append(row[2])

