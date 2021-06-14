'''
 If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.
'''

temperature = int(input("enter the room temperature: " ))
if temperature > 30:
    print("its a hot day")
elif temperature < 10:
    print("its cold day")
else:
    print("its neither hot nor cold")