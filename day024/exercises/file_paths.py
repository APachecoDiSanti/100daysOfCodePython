# Absolute path
with open("/home/user/Documents/my_file.txt") as file:
    print(file.read())

# Relative path
with open("../../../../../Documents/my_file.txt") as file:
    print(file.read())
