
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""
	This function takes in two lists of equal length, height and weight, and returns a list of the BMI values of the
	corresponding elements in the two lists. The formula for BMI is weight / (height * height) where weight is in
	kilograms and height is in meters.
	"""
	try:
		if len(height) != len(weight):
			raise ValueError("Height and weight lists must be of equal length")
	except ValueError as e:
		print(e)
		return None
	return([weight[i] / (height[i] * height[i]) for i in range(len(height))])

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""
	This function takes in a list of BMI values and a limit, and returns a list of booleans indicating whether the
	corresponding BMI value is greater than the limit.
	"""
	try:
		if type(limit) != int:
			raise ValueError("Limit must be an integer")
	except ValueError as e:
		print(e)
		return None
	return([bmi[i] > limit for i in range(len(bmi))])
