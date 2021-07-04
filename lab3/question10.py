'''
Write a program to find the factorial of a number using functions.
'''

def factorial() :
    num = int(input("enter the value:"))
    fac = 1
    while num > 0 :
     fac = fac * num
     num = num-1
    print("facrotial:" ,fac)
factorial()