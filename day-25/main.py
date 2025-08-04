"""
main.py: Day 25 main python codebase
"""
# import csv
#
# with open('weather_data.csv', mode='r') as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for idx, temp in enumerate(data):
#         if idx != 0:
#             temperatures.append(int(temp[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')

# Getting a column
# print(data["condition"])
# print(data.condition)

# Getting a row
# print(data[data.day == "Monday"])

# Printing the row of data which had highest temperature
# print(data[data.temp == data.temp.max()])

# monday_temp = data[data.day == "Monday"].temp[0]
# monday_temp = monday_temp * 9/5 + 32
# print(monday_temp)

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Chukwuemeka", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

"""
New York Central Park Population Data analysis
"""
squirrel_data = pandas.read_csv('squirrel_data.csv')


squirrel_counts = squirrel_data["Primary Fur Color"].value_counts()
squirrel_counts.to_csv('squirrel_count.csv')


