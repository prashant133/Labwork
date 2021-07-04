'''
write the function called fizz_buzz that takes a nubmer.
if the number is divisible by 3 , it should return fizz
if the number is divisible by 5 its should return buzz
if it is divisible by both 3 and 5 it should return fizzbuzz
other wise its should return the same number.
'''
def fizz_buzz(num1):
    if num1 % 3 == 0 and num1 % 5 == 0 :
        return "fizzbuzz"
    if num1 % 3 == 0:
        return "fizz"
    if num1 % 5 == 0 :
        return "buzz"
    return num1
num1 = int(input("enter the number: "))
print(fizz_buzz(num1))