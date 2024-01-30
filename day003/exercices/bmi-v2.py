# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)

if bmi < 18.5:
  category = "you are underweight."
elif bmi < 25:
  category = "you have a normal weight."
elif bmi < 30:
  category = "you are slightly overweight."
elif bmi < 35:
  category = "you are obese."
else:
  category = "you are clinically obese."
print(f"Your BMI is {bmi}, {category}")
