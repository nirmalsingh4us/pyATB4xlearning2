def new_prog(a,b):
  return a + b

result = new_prog(5,20)
print(result)

num = int(input("Enter the int number\n"))
# fact = 1
# if num == 0 or num == 1:
#   fact = 1
#  print(1)
# else:
for num in range(0, num + 1, 1):
    fact = num * num
    print(fact)