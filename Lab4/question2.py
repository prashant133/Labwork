'''
2.Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)
'''

temperature = int(input("enter the temperature: "))
unit= input("(F) or (C): ")
if unit.upper() == "F" :
    converted_celsius = (5/9) * (temperature-32)
    print(converted_celsius,"celsius is the temperature of the person")
elif unit.upper() == "C" :
    converted_fahrenheit = ((9 * temperature)+160)/5
    print(converted_fahrenheit,"fahrenheit is the temperature of the person")
