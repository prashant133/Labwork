'''
  Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise
   they need to put down 20%.
 '''
price = 100000
good_credit = True
if good_credit:
     credit = 0.1 * 100000
     print(f'buyer has to pay 10 % ')
else :
    credit = 0.2 * 100000
    print(f'buyer has to pay 20 %')

