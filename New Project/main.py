from random import randint
totalrange = 1000
win=0
def revealGivenChoice(choice,prize):
	if choice == prize:
		if choice == 1:
			return randint(2,3)
		elif choice == 2:
			var = randint (1,2)
			if var == 1:
				return 1
			else:	
				return 3
		else:
			return randint(1,2)

	elif choice == 1:
		if prize == 2:
			return 3
		else:	
			return 2

	elif choice == 2:	
		if prize == 1:
			return 3
		else: 
			return 1

	else:
		if prize == 2:
			return 1
		else:
			return 2

def switch(choice,reveal):
	if choice == 1:
		if reveal == 2:
			return 3
		else: 
			return 2	
	elif choice == 2:
		if reveal == 1:
			return 3
		else:
			return 1
	else:
		if reveal == 1:
			return 2
		else:
			return 1	
	



for i in range(0,totalrange):
	prizedoor = randint(1,3)
	doorchoice = randint(1,3)
	reveal = revealGivenChoice(prizedoor,doorchoice)
	print "You chose door" + str(doorchoice) + "\n"
	print "I revealed " + str(reveal) + "\n"
	print "You switch."
	doorchoice = switch(doorchoice,reveal)
	if doorchoice == prizedoor:
		win += 1
		print "You Win"
		
	else: 
	    print "You Lose"
		

print "You won " + str(win) + " out of " + str(totalrange)
	
	
		


