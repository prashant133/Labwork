'''
8. Given a three-digit number. Find the sum of its digits.
'''
number = int(input('Enter the three digit number: '))
a = number // 100
b = number // 10 % 10
c = number %10
sum_of_digits=(a+b+c)
print(f'The sum of digits is:{sum_of_digits}')

#using loop
number = int(input('enter the number: '))
sum = 0
while number > 0 :
    sum = sum + number % 10
    number = number//10
print("sum of digits=",sum )
