'''
Task -----------------condition------------------------------
Weight converter:
  Input the weight of a person in either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs
  else convert it to kg.
'''
weight = int(input("Enter the weight of the person : "))

unit = input("(L)bs or (K)g : ")

if unit.upper() == "L":
    converted_lbs = weight * 0.45
    print(f"The person weight is {converted_lbs} kilos")
elif unit.upper() == "K":
    converted_kg = weight / 0.45
    print(f"The person weight is {converted_kg} pounds")
else:
    print(f"Please enter appropriate character as K for Kg or L for Lbs !!")