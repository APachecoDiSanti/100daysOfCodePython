with open("weather_data.csv", "r") as weather_csv:
    weather_data = weather_csv.readlines()

print(weather_data)

import csv

with open("weather_data.csv", "r") as weather_csv:
    weather_data = csv.reader(weather_csv)
    temperatures = []
    for row in weather_data:
        print(row)
        temp = row[1]
        if temp != "temp":
            temperatures.append(int(row[1]))

print(temperatures)
