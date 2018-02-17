

#This is a comment
'''
	This
	is 
	multiline
	comment
'''

#lets start by creating a string of our characters
abc = "abcdefghijklmnopqrstuvwxyzåäö"

#now lets take the user input


user_inp = input("Enter your word: ")
sum_all = 0

for x in user_inp:
	index_position = abc.index(x) + 1 
	print("%s : index: %d" % (x, index_position))
	sum_all = sum_all + index_position

print("Sum: " + str(sum_all))

def find_numeric(s):
	if(s<10):
		# if s<10 than s is single digit 
		return s
	else:
		ss = str(s) #we convert the number to a string for easy manipulation
		sum_this =0
		for x in ss:
			sum_this += int(x)

		return find_numeric(sum_this)
	
print("Numeric value: " + str(find_numeric(sum_all)))

