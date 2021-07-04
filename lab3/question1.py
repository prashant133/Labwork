'''
write the python code to find the max of three numbers.
'''

def max(x,y,z):
    if x > y and x > z :
        return x
    elif y > x and y > z :
        return y
    elif z > x and z > y :
        return z
x = int(input("enter the number: "))
y =  int(input("enter the number: "))
z =  int(input("enter the number: "))
max(x, y, z)
print(max(x,y,z),"is the max number")