import pandas

weather_data = pandas.read_csv("weather_data.csv")
print(weather_data["temp"])

weather_dict = weather_data.to_dict()
print(weather_dict)

temp_list = weather_data["temp"].to_list()
print(temp_list)

average_temp = sum(temp_list)/len(temp_list)
print(average_temp)

print(weather_data["temp"].mean())
print(weather_data["temp"].max())

print(weather_data["condition"])
print(weather_data.condition)

print(weather_data[weather_data.day == "Monday"])
print(weather_data[weather_data.temp == weather_data.temp.max()])

monday_data = weather_data[weather_data.day == "Monday"]
print(monday_data.temp[0] * 1.8 + 32)

# Create a Dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
