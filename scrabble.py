def letterScore(letterScore):

	if letterScore in 'qzQZ':
		return 10

	elif letterScore in 'aeilnorstuAEILNORSTU':
		return 1

	elif letterScore in 'dgDG':
		return 2

	elif letterScore in 'bcmBCM':
		return 3

	elif letterScore in 'fhvwyFHVWY':
		return 4

	elif letterScore in 'jxJX':
		return 8
	
	else:
		return 0

def wordScore():

	userInput = input("enter a word")
	score=0
	for i in range(0, len(userInput)): 

		score += letterScore (userInput[i])


	print(score)