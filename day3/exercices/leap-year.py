# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
divisble_by_4 = (year % 4) == 0
divisble_by_100 = (year % 100) == 0
divisble_by_400 = (year % 400) == 0

if divisble_by_4 and not divisble_by_100:
  print("Leap year")
elif divisble_by_100 and divisble_by_400:
  print("Leap year")
else:
  print("Not leap year")
