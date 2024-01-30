target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
if (target < 0 or target > 1000):
  print("Input must be between 0 and 1000 (inclusive)!")
else:
  sum = 0
  for number in range(1, target+1):
    if number % 2 == 0:
      sum += number
  print(sum)
