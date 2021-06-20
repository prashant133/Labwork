'''
given three integers, print the smallest one. (three integers should be user input).
'''

first_integer = int(input(f'Enter the first number: '))
second_integer = int(input(f'Enter the second number: '))
third_integer = int(input(f'Enter the third number: '))

if first_integer < second_integer and first_integer < third_integer :
    print(f'First integer is smallest.')
elif second_integer < first_integer and second_integer < third_integer :
    print(f'Second integer is smallest.')
else :
    print(f'Third integer is smallest.')