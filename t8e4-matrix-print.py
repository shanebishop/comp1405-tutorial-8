#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Prints x (assumes x is a matrix)
def printMatrix(x):
	# If x is empty, print an error message
	# (Maybe a better test would be "len(x) == 0")
	if x == []:
		print("ERROR! The passed argument is an empty list.")
	# Otherwise, print x
	else:
		for i in range(len(x)):
			# Print initial "|" character, followed by a space
			print("| ", end="")
			
			# Print the current element in x[i]
			for j in range(len(x[i])):
				print(x[i][j], end=" ")
			
			# Print final "|"
			print("|")