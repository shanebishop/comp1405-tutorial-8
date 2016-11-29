#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

from types import isinstance

# Determines if x is a matrix
def isMatrix(x):
	# If x is rectangular and numeric, return true
	if isRectangular(x) and isNumeric(x):
		return True
	# Else, return false
	else:
		return False

# Borrowed from earlier
def isRectangular(x):
	row_length = -1
	for i in range(len(x)):
		if row_length == -1:
			row_length = len(x[i])
		elif row_length != len(x[i]):
			return False
	return True

# Borrowed from earlier
def isNumeric(x):
	for i in range(len(x)):
		for j in range(len(x[i])):
			if not isinstance(x[i][j], (int, float)):
				return False
	return True