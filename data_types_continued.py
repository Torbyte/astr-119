s = "I am a string"
print("The type of s is ",type(s))

#boolean
yes = True 
print("The type yes is ",type(yes))
no = False
print("The type no is ",type(no))


alpha_list = ["a", "b", "c"]
print("The type of alpha_list is", type(alpha_list))
print("The type of alpha_list[0] is", type(alpha_list[0]))
alpha_list.append("d")
#adds d to list
print(alpha_list)
#tuple is unchangeable list
alpha_tuple = ("a", "b", "c")
print("The type of alpha_tuple is", type(alpha_tuple))
print("The type of alpha_tuple[0] is", type(alpha_tuple[0]))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("We can't change a tuple")
print(alpha_tuple)
