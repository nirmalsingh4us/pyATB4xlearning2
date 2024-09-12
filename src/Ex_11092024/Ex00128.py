# file handling
# Read and write content
# read a file
# reading entire content : content = file_object.read()
# line = file_object.readline()  for a single line
# lines = file_object.readlines()  for all lines in a list
# close the file
import os

full_path_file = os.path.join("C:\Users\NIRMAL\PycharmProjects\pyATB4xlearning\src\Ex_11092024\NS_TEST\",NS.txt")
file = open(full_path_file, 'r')
content = file.read()
print(content)
