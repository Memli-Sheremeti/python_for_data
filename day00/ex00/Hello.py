ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = "World!"

def ft_modify_a_tuple(ft_tup, index, dest):
    lst = list(ft_tup)
    lst[index] = dest
    return tuple(lst)

ft_tuple = ft_modify_a_tuple(ft_tuple, 1, "France!")

ft_set.remove("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
