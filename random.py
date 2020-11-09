from random import randint

randval = randint(0, 10)
counter = 1

inputval = input("Guess The Number: ") 
inputvalint = int(inputval)
print(inputvalint) 

if inputvalint == randval:
	print("You Guessed Right! CONGRATULATIONS! :)")
	print("Your tries:" + str(counter))
elif inputvalint > randval:
	print("Too High :(")
else:
	print("Too Low :(")
	
values = [inputvalint]
counter += 1

while inputvalint != randval:
	inputval = input("Guess The Number: ") 
	inputvalint = int(inputval)
	print(inputvalint) 
	if inputvalint == randval:
		print("You Guessed Right! CONGRATULATIONS! :)")
		print("Your tries:" + str(counter))
	elif inputvalint > randval:
		print("Too High :(")
	else:
		print("Too Low :(")
	if inputvalint not in values:
		values.append(inputvalint)	
		counter += 1
