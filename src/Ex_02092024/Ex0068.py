# list is mutalbe in nature
# list use more memory  where tuple use less memonry
# defined with [] where tupel define ()
# tuple is fast in compare list.
# list have dynamic where tuple is static
squares = [1,4,9,16,25]
squares[3]=64
print((squares))

#tuple is unmutalbe in nature
#my_tuple = (1,4,9,16,25)
#my_tuple[3]=64
#print(my_tuple)

my_tpl = ("ais.com","cm.com")
print(my_tpl)
dm_list = list(my_tpl)
print(dm_list)
my_tpl = tuple(dm_list)
print(my_tpl)
