age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_int = int(age)
MAX_AGE = 90
WEEKS_IN_YEAR = 52
weeks_left = (MAX_AGE - age_int) * WEEKS_IN_YEAR
print(f"You have {weeks_left} weeks left.")
