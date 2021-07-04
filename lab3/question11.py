'''
Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]
'''
def armstrong():
    i = int(input("Enter the number: "))
    orig = i
    sum = 0
    while i > 0 :
        sum = sum + (i%10)*(i%10)*(i%10)
        i = i//10
    if orig == sum :
        print([sum],"this is armstrong")
    else:
        print([sum],"this is not armstrong")
armstrong()
