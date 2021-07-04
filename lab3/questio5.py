'''
write the function called show_star(rows).if the row is 5 then it should print the following.
*
* *
* * *
* * * *
* * * * *
'''
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
