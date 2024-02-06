sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
list = sentence.split()

result = {word: len(word) for word in list}

print(result)
