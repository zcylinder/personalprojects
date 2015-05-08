''' This program takes an integer and determines
	whether predetermined rope lengths can be made
	the same size as the integer.
	
	Algorithm:
	-Generate possible permutations of the ropes
	-Add permutations together and place in new list
	-Compare integer n to the list to see if there is a match.
	
	@Author: Zack Cylinder
	@Last modified: April 20, 2015 10:16PM
'''

lengths = [2, 5, 6, 6] #These are the lengths of given ropes

'''The method below generates permutations in the following ways:
	--Skip over any numbers less than or equal to zero.
	--Append the current (ith) integer to a list, if not already in the list.
	--Add the current integer to the other integers in the list individually, 
		and append them if not already in the list.
	--Add the current integer to multiple integers in the list 
	(ex: i + (i+1) + (i+2)) and append if not already in the list.
	--Repeat until the list of ropes has been iterated through.
'''

def ropes(list):
	permuted = [] #This is the list of permutations of rope lengths without repetition
	sum = 0 #This keeps track of sum of ints in the list sequentially
	
	for i in range(0, len(list)): 
		if list[i] <= 0:
			continue
			
		if list[i] not in permuted:
			permuted.append(list[i])
		
		n = i + 1
		while n < len(list):
			if list[i] + list[n] not in permuted:
				permuted.append(list[i] + list[n])
			n += 1
		
		sum += list[i]
		if sum not in permuted:
			permuted.append(sum)
	
	return permuted		
			
#Iterates through permuted list and checks for a match with the given number
def check_int(n):
	permuted = ropes(lengths)
	for i in range(0, len(permuted)):
		if n == permuted[i]:
			return True
	else:
		return False

if check_int(18) == True:
	print 'You got a match!'
else:
	print 'Sorry, no match!'
