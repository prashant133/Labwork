'''
For given integer x, print "true" if it is positive print "false" if it is negative and print "zero" if it is 0.
'''

number = int(input(f'Enter the number: '))
if number%2 == 0 :
    if number == 0:
        print(f'The number is zero.')
    else:
        print(f'true.')
else :
    print(f'false.')
