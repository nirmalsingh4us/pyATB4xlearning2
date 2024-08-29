# Write a program that print num from 1 to 100,
# loop for num, for multiple of 3 print "fizz"
# for multiple of 5 print 'buzz'
# For nub that are multiple for both 3 & 5 print 'fizzbuzz'

for i in range(1, 100):
    if (i % 3 == 0 and i % 5 == 0):
        print("Fizzbuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("buzz")
    else:
        print(i)
