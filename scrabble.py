def letterScore(letterScore):

	if letterScore in 'qz':
		return 10

	elif letterScore in 'aeilnorstu':
		return 1

	elif letterScore in 'dg':
		return 2

	elif letterScore in 'bcm':
		return 3

	elif letterScore in 'fhvwy':
		return 4

	elif letterScore in 'jx':
		return 8
	
	else:
		return 0

def wordScore():

	userInput = input("enter a word")
	score=0
	for i in range(0, len(userInput)): 

		score += letterScore (userInput[i])


	print(score)
