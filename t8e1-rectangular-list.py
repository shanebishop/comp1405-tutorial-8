#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Returns true if x is rectangular; false if otherwise
def isRectangular(x):
	# Initialize the row length to a negative number to help with debugging
	row_length = -1
	
	# Iterate through the list and check to see if each sublist is the same length
	for i in range(len(x)):
		# Intialize row_length to the length of the first row encountered
		if row_length == -1:
			row_length = len(x[i])
		# If the row length of the current row is different from the previous, return false
		elif row_length != len(x[i]):
			return False
	
	# Since we haven't returned anything yet, the lengths must be the same; return true
	return True