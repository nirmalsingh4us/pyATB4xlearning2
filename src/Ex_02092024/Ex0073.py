t = ("Adroit","Infosystem","Adroit")
print(t)
print(set(t))

# union set example
set1 = {1,2,3,4}
set2 = {4,5,6,8}
my_set = set1.union(set2)
print(my_set)

set3 = {1,2,3,4,5,6}
set4 = {4,5,6,7}
my_set1 = set3.intersection(set4)
print(my_set1)

my_set = set1.difference(set2)
print(my_set)

set1 = {1,2,3,4,5,8}
set2 = {2,3,8}
subset = set2.issubset(set1)
print(subset)