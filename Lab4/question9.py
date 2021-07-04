'''
9.Write a program to find the factorial of a number.
'''
num = int(input("enter the value: "))
factorial = 1
while num > 0 :
    factorial = num * factorial
    num = num -1
print('factorial:',factorial,)