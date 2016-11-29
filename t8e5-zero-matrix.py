#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Returns a square matrix with x rows and x cols
def zeroMatrix(x):
	# Intialize return value
	retval = []
	
	# Initializes return value
	for i in range(x):
		# Intialize a new row
		new_row = []
		
		# Append 0s to new row
		for j in range(x):
			new_row.append(0)
		
		# Append new row
		retval.append(new_row)
	
	# Return the return value
	return retval