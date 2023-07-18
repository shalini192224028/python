sentence = input("Enter a sentence: ")

count = 0

for char in sentence:
    if char == 'A':
        count += 1

print("The number of capital 'A' in the sentence is:", count)
