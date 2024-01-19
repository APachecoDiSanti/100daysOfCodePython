# Write your code below this line 👇
# Naive, algorithm. 
# Some optimizations can be done such as checking it's divisible by 2 and no other even number.
def prime_checker(number):
  is_prime_number = True
  for i in range(2,number):
    if number % i == 0:
      is_prime_number = False
  if is_prime_number:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
