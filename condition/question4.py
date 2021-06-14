'''
Task -----------------condition------------------------------
Weight converter:
  Input the weight of a person in either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs
  else convert it to kg.
'''
weight_of_person_in_kg = int(input("enter the weight of person: "))
weight_in_pound = weight_of_person_in_kg / 0.45
print(weight_in_pound)
print(f"the weight of the person in kg is {weight_in_pound }")