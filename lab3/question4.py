'''
write the functions that returns the multiple of 3 and 5 between 0 and limit (parameter).
for example
if the limit is 20 its should return the sum of 3,5,6,9,10,12,15,18,20
'''

def sum_of_numbers(limit):
    total = 0
    for i in range(limit+1):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i

    return total
limit = int(input("Enter limiting number: "))
print(sum_of_numbers(limit))

