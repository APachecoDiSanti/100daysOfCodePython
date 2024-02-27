from data_manager import *

data_manager = DataManager()

print("Welcome to Agustin's Flight Club")
print("We find the best flight deals and email you")
user_first_name = input("What is your first name?\n")
user_last_name = input("What is your last name?\n")
user_email = input("What is your email?\n")
user_email_copy = input("Type your email again.\n")

if user_email == user_email_copy:
    data_manager.register_user(user_first_name, user_last_name, user_email)
    print("You're in the club!")
else:
    print("Oops! The emails don't match!")
