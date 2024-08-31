# list example
my_shopping_list = ["Sugar", "Tea", "milk"]
print(my_shopping_list)
print(my_shopping_list[2])


def bring_more_food(my_list):
    more_item = input("enter the item\n")
    my_list.append(more_item)
    return my_list


list = bring_more_food(my_shopping_list)
print(list)
