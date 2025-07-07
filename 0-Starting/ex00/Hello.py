ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_dict["Hello"] = "42Paris!"
#Tuples are immutable, so you cannot change their values, but you can assign a new tuple to the variable
ft_tuple = ("Hello", "France!")
#Sets are unordered, so you cannot be sure in which order the items will appear
ft_set.remove("tutu!")
ft_set.add("Paris!")


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)