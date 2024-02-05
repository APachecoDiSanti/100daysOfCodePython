# Both files contain 1 int number per line
file_1 = open("file1.txt").readlines()
numbers_1 = [int(n.strip()) for n in file_1]

file_2 = open("file2.txt").readlines()
numbers_2 = [int(n.strip()) for n in file_2]

result = [n for n in numbers_1 if n in numbers_2]

# Write your code above 👆
print(result)
