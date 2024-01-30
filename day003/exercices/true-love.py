print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1_upper = name1.upper()
name2_upper = name2.upper()
score1 = 0
score2 = 0

score1 += name1_upper.count("T")
score1 += name1_upper.count("R")
score1 += name1_upper.count("U")
score1 += name1_upper.count("E")
score1 += name2_upper.count("T")
score1 += name2_upper.count("R")
score1 += name2_upper.count("U")
score1 += name2_upper.count("E")

score2 += name1_upper.count("L")
score2 += name1_upper.count("O")
score2 += name1_upper.count("V")
score2 += name1_upper.count("E")
score2 += name2_upper.count("L")
score2 += name2_upper.count("O")
score2 += name2_upper.count("V")
score2 += name2_upper.count("E")

score = int(f"{score1}{score2}")

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
