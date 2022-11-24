# import csv
#
# with open('weather_data.csv') as weather_csv:
#     data = csv.reader(weather_csv)
#     temperature = []
#
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

# data = pandas.read_csv('weather_data.csv')
#
# temp_dict = data['temp'].to_dict()
# print(temp_dict)
#
# print(data['temp'].max())
#
# print(data[data.temp == data['temp'].max()])

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])

data_dict = {
    "Fur Color": ['Gray', 'Red', 'Black'],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count_data_cleaned.csv")