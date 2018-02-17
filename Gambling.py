money = 2000

import random

def gamble():
	global money
	print("You have: $"+str(money))
	
	print("How much do you want to gamble?")
	amount = int(input("Amount you want to gamble"))
	if money < amount:
		print("You are broke"); return 0

	pivot = int(input("Enter the pivot point(1-100): "))
	low_high = input("low or high?")

	pc_num = random.randint(1,100) # generate a random number between 1-100
	print("Cpu rolled: %d"%  pc_num)

	if low_high == "low":
		if(pc_num< pivot):
			print('you win')
			if pivot>50:
			money = amount+(money+abs(pivot-50))
			else:
			money = amount+(money+abs(pivot-50))
			 #money + amount +  float((100-pivot)/100)*amount
		else:
			print('You lost')
			money = money - amount

	elif low_high == "high":
		if(pc_num>pivot):
			print('you win')
			money= money + amount +  float(100/(100-pivot))*amount

		else:
			print('you lost')
			money =  money - amount

	
	print("You have: $"+str(money))
	

while(money>0):
	if money > 0:
		gamble()
	else:
		print("You wasted all your money fool")
