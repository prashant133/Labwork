'''
wrtie the function called showNumber that takes parameter call limit.
it should print all the number between 0 and limit with a label to identify even and odd.
for exaample if the number is 3,it should print:
o even
1 odd
2 even
'''

def showNumber(limit) :
    for i in range (limit+1):
        if i % 2 == 0 :
            print(limit,"even")
        if i % 2 != 0 :
            print(limit,"odd")
showNumber()
limit = int(input('Enter the value : '))
print(showNumber(limit))