# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum = 0
items = 0
for heigth in student_heights:
  sum += heigth
  items += 1
print(f"total height = {sum}")
print(f"number of students = {items}")
print(f"average height = {round(sum/items)}")
