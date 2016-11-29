#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Creates a square identity matrix
def identityMatrix(x):
	# Intialize return value
	retval = []
	
	# Initializes return value
	for i in range(x):
		# Intialize a new row
		new_row = []
		
		for j in range(x):
			# If this is where we want to 1, append 1
			if j == i:
				new_row.append(1)
			# Otherwise, append 0
			else:
				new_row.append(0)
		
		# Append new row
		retval.append(new_row)
	
	# Return the return value
	return retval