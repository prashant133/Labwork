'''
Write a Python function that takes a number as a parameter and check the number is prime or not
'''

'''num = int(input("Enter the number: "))
# prime numbers are greater than 0
if num > 0:
    # check for factors
    #if the count is 2 then it sis prime number.
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")'''
def prime(num):

    for i in range(2,num):
        if num % i ==0:
            print(num,"is not the prime number.")
            print(i,"times",num//i,"is",num)
        break
    else:
        print(num,"is the prime number.")
num = int(input("enter the number: "))
prime(num)