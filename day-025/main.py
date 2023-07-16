#data = []
#with open("weather_data.csv") as csv_file:
#    line = csv_file.readlines()
#    data.append(line)

#import csv
#with open("weather_data.csv") as csv_file:
#    data = csv.reader(csv_file)
#    temperatures = []
#    for row in data:
#        print(row)
#        temperatures = [int(row[1]) for row in data if row != "temp"]

import pandas as pd
data = pd.read_csv("weather_data.csv")
print(type(data))
print("Mean of temperature = ", data["temp"].mean())
print("Max of temperature = ", data["temp"].max())
print("Min of temperature = ", data["temp"].min())
print("\n",data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
print(monday.condition)

new_monday_temp = monday.temp.values * 1.8 + 32
print(f"{monday.temp.values} oC is converted to {new_monday_temp} F!")
monday.temp = new_monday_temp
print(monday)