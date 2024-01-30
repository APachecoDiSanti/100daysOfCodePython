#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""
for n in range(1, nr_letters + 1):
    rand_index = random.randint(0, len(letters) - 1)
    easy_password += letters[rand_index]

for n in range(1, nr_symbols + 1):
    rand_index = random.randint(0, len(symbols) - 1)
    easy_password += symbols[rand_index]

for n in range(1, nr_numbers + 1):
    rand_index = random.randint(0, len(numbers) - 1)
    easy_password += numbers[rand_index]

print(f"Easy password: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# My strategy: 
# Pick randomly between letters, symbols or numbers
# Then pick a random character from that list
# Make sure to keep track how many characters you may add from each list so you don't add more/less than asked
hard_password = ""
nr_characters = nr_letters + nr_symbols + nr_numbers

for n in range(0, nr_characters):
    available_characters = []
    if nr_letters > 0:
        available_characters.append(letters)
    if nr_symbols > 0:
        available_characters.append(symbols)
    if nr_numbers > 0:
        available_characters.append(numbers)

    # Next character is a letter, symbol or number?
    rand_available_characters_index = random.randint(0, len(available_characters) - 1)
    rand_character_list = available_characters[rand_available_characters_index]

    # Next character is a random item from the chosen character list
    rand_index = random.randint(0, len(rand_character_list) - 1)
    next_character = rand_character_list[rand_index]
    hard_password += next_character

    if rand_character_list == letters:
        nr_letters -= 1
    elif rand_character_list == symbols:
        nr_symbols -= 1
    else:
        nr_numbers -= 1

print(f"Hard password: {hard_password}")
