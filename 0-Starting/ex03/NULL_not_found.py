import math

def NULL_not_found(object: any) -> int:

	if type(object) == float and math.isnan(object):
		print(f"Cheese: {object} {type(object)}")
	elif object is None:
		print(f"Nothing: {object} {type(object)}")
	elif type(object) == bool:
		print(f"Fake: {object} {type(object)}")
	elif object == 0:
		print(f"Zero : {object} {type(object)}")
	elif type(object) == str and object == '':
		print(f"Empty: {type(object)}")
	else:
		print("Type not Found")
		return 1
	return 0

	