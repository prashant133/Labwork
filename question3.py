'''
3. N students take K apples and distribute them among each other evenly.
The remaining (the undivisible) part remains in the basket. How many apples will each single student get?
 How many apples will remain in the basket? The program reads the numbers N and K.
 It should print the two answers for the questions above.
'''

N=int(input("enter the number of the student: "))
K=int(input('enter the number of apples: '))
print(f'the apples tha each student will get is {K//N}  ')
print(f'the remaining appels in the basket is {K%N}')


































