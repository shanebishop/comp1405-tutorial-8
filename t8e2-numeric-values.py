#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

from types import isinstance

# Returns true if all of the elements in x are numeric; false if otherwise
def isNumeric(x):
	# Iterate through x looking for non-numeric elements
	for i in range(len(x)):
		for j in range(len(x[i])):
			# If a non-numeric element is found, return false
			if not isinstance(x[i][j], (int, float)):
				return False
	# Since we haven't returned anything yet, all elements must be numeric; return true
	return True