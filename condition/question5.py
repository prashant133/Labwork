'''
game finding a secret number within 3 attempts using while loop
'''
import random
secret_number = random.randint(1,10)
total_number_of_attempt = 3
number_of_attempt = 0
while number_of_attempt < 3:
   guess = int(input('enter the number::'))

   if secret_number!= guess:
       print(f"This is not the number: ")
       number_of_attempt += 1
   else:
       print(f"congrats!!!you guessed the number.")
       break
if number_of_attempt == 3:
        print(f'you lose. loser!!')
