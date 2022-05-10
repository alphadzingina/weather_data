# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
#data = pandas.read_csv("weather_data.csv")
#print(data)
#print(data['temp'])

#temp_list = data['temp']

#average = sum(temp_list) / len(temp_list)

# print(data['temp'].mean())
# max_temp = (data['temp'].max())

# print(data[data.temp == max_temp])
# monday = data[data.day == 'monday']
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp + 9/5 + 32
# print(monday_temp_F)

#create a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
