'''
8. Write a Python program which accepts the radius of a circle from the user and compute the area.
 (area of circle = PI * r2)
'''
PI = 3.14
radius = int(input('enter the radius: '))
area = PI * radius ** 2
print(f'the area of a circle is {area}')