import sys

try:
	try:
		if len(sys.argv) < 2:
			exit()
		num = int(sys.argv[1])

	except ValueError:
		raise AssertionError("argument is not an integer")
	
	if len(sys.argv) != 2:
		raise AssertionError("more than one argument is provided")
	
	if num % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

# If an AssertionError occurs, the except code will be executed
except AssertionError as error:
	# The message includes the name of the error and the error message associated
    print(AssertionError.__name__ + ":", error)
