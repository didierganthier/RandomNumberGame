import random

random_number = random.randint(0,9)
choice = 3
while choice > 0:
	user_input = input('Guess a number between 0 and 9\n')
	user_input = int(user_input)
	if user_input == random_number:
			print('Well guessed, it was',random_number)
			choice = 0
	elif user_input > random_number:	
			choice -= 1
			print('Too big, try again\n')
	elif user_input < random_number:	
			choice -= 1
			print('Too small, try again\n')		
			
	else:	
			print('No choices left, sorry')	
			choice = 0