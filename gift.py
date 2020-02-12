import random

numPeople=int(input("How many people are playing?"))
givers =[]
receivers = []
print("Please enter their names:")

#read input names
for i in range(numPeople):
	givers.append (input(""))

#duplicate list
receivers = givers[:]

print()
print("Gift Assignments...")
match=[]
k=0

#printing first pair to prevent duplicates and loops
match = [givers[0], "will buy a gift for", receivers[-1]]
print(match)
receivers.pop(-1)
givers.pop(0)
random.shuffle(receivers)
while len(receivers)>0:


	#comparing for same person name. if same name replace with random
	if(givers[k]==receivers[k]):
		j=random.choice (receivers)
		match = [givers[k], "will buy a gift for", j]
		givers.pop(k)
		receivers.remove(j)



	elif (givers[k]!=receivers[k]):
		match = [givers[k], "will buy a gift for", receivers[k]]
		receivers.pop(k)
		givers.pop(k)


	k+1	
			
#printing match list with the results
	print(match)


