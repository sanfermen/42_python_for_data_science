
def slice_me(family: list, start: int, end: int) -> list:
	if not isinstance(family, list):
		raise ValueError("The first argument must be a list.")
	if not isinstance(start, int) or not isinstance(end, int):
		raise ValueError("The second and third arguments must be integers.")
	if start < 0 or end < 0:
		raise ValueError("The second and third arguments must be positive integers.")
	if start > end:	
		raise ValueError("The second argument must be less than the third argument.")
	if end > len(family):
		raise ValueError("The third argument must be less than the length of the list.")
		