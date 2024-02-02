with open("my_file.txt") as file:
    file_contents = file.read()
    print(file_contents)

with open("my_file.txt", mode="w") as file:
    file.write("what's up?")

with open("my_file.txt", mode="a") as file:
    file.write("\nappending")

with open("new_file.txt", mode="w") as file:
    file.write("Writing on a new file!")
