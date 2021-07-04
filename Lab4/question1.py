'''
Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''
lower = 1500
upper = 2700
for i in range(lower,upper+1):
    if (i%5==0 and i%7==0):
        print(i)



