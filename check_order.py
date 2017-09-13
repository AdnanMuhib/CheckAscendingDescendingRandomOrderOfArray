'''
Assignment: given an integer array 

check whether the given array is in 

a. Ascending order
b. Descending order
c. Random order
Submitted by : Muhammad Adnan Mohib
Registration Number: 2015-CS-51

'''

# check whether array has Ascending Order
# Params: array of integers
# return bool

def isAscending(arr):
	for i in range(len(arr)-1):
		if (arr[i] >= arr[i+1] ):
			return False
	return True

# check whether array has Descending Order
# Params: array of integers
# return bool
def isDescending(arr):
	for i in range(len(arr)-1):
		print(arr[i], arr[i+1])
		if (arr[i] <= arr[i+1] ):
			return False
	return True


# Main Function to Drive the Program
if __name__ == '__main__':
	
	# input the size of the array from the user
	size_of_array = input("Enter the Size of the Array: ")
	# declare an array to store the numbers
	arr = []
	# take input and append that to the array of numbers
	for i in range(size_of_array):
		arr.append(input(str(i) + ": "))
	# check whether the size of the array only one
	# that means we can't determine whether the array is ascending,
	# descending or in random order
	if(len(arr) == 2):
		print("only ascending or descending order will be checked" +
		 "\nbecause size of the array is 2 which can't detemine random order.")
	
	if(len(arr) <= 1):
		print("can't determine because array has only one element or no element..")
	else:
		if(isAscending(arr)):
			print("Array has Ascending Order")
		elif(isDescending(arr)):
			print("Array has Descending order")
		else:
			print("Random Order")