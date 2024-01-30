# Write your code here 👇
for number in range(1,100+1):
  msg = ""
  if number % 3 == 0:
    msg +="Fizz"
  if number % 5 == 0:
    msg +="Buzz"
  if msg == "":
    msg = str(number)
  print(msg)
