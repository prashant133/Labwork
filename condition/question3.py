'''
  If name is less than 3 characters long- name must be at least 3 characters
  otherwise if it's more than 50 characters - name must be maximum of 50 characters
  otherwise - name looks good!
'''
char = (input("enter the name: "))
print(f'the length of name is:{(len(char))} ')
if len(char)<= 3:
    print('so name must be long ')
elif len(char)> 50:
    print('so name is long')
else :
    print("so name is good")

