'''
Write a program that reads the length of the base and the height of a right-angled triangle and prints the area.
Every number is given on a separate line.
'''

length=int(input('enter the length of triangle '))
breadth=int(input('enter the breadth of triangle '))
area=(length*breadth)//2
print(f'the area of triangle of length {length} and breadth {breadth} is {area} ')