weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: round(celsius*(9/5)+32, 1) for (day, celsius) in weather_c.items()}


print(weather_f)
