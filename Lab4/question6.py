'''
Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
even = 0
odd = 0
lower = int(input("enter the lower range: "))
upper = int(input("enter the upper range: "))
for i in range(lower,upper+1):
    if i%2 == 0 :
        even += 1

    else:
        odd += 1

print("even:", even)
print("odd:", odd)
