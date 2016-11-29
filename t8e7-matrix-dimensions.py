#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Returns true of x and y have the same number of rows and cols
def sameSize(x, y):
	# If the lengths differ, return false
	if len(x) != len(y):
		return False
	else:
		# If the lengths of x[i] and y[i] ever differ, return False
		for i in range(len(x)):
			if len(x[i]) != len(y[i]):
				return False
		
		# Otherwise, return true
		return True