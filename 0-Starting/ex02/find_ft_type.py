def all_thing_is_obj(object: any) -> int:
	types_dict = {list : "List", tuple : "Tuple", set : "Set", dict : "Dict"}

	# Determine the type of the given object
	object_type = type(object)
	# Get the name of the object or print "Type not found" if not present
	types = types_dict.get(object_type, "Type not found")

	if object_type == str:
		print(f"{object} is in the kitchen : {object_type}")
	elif types != "Type not found":
		print(f"{types} : {object_type}")
	else:
		print(types)

	return 42