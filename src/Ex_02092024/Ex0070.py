a, b, c = (7, 8, 9)
print(a)
print(b)
print(c)

# search in tuple
cities = ("Delhi", "Mohali", "Amritsar")
print("chd" in cities)


# append in tuple
t = (8,4,2)
#t.append(12) can't append in tuple, convert tuple into list then make append.
my_list = list(t)
my_list.append(16)
t = tuple(my_list)
print(t)