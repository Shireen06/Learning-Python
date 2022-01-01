# -*- coding: utf-8 -*-
import csv
import pandas as pd
from statistics import mean

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
            
#     print(temperatures)

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# print(data)

# data_dic = data.to_dict()
# print(data_dic)

# temp_list = data["temp"].to_list()
# list_avg = mean(temp_list)
# print(list_avg)

# print(data["temp"].mean())

# print(data["temp"].max())
# print(data.condition)

# Get data from a row

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)

# Create a df from scratch

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
    }
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
# print(data)


