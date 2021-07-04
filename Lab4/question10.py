'''
Write a Python program that accepts a string and calculate the number of digits and letters
'''
word = input("enter the word: ")
letter = 0
digit = 0
for i in word:
    if i.isdigit():
        digit = digit + 1
    elif i.isalpha():
        letter = letter + 1

print("letters:",letter)
print("digits:",digit)