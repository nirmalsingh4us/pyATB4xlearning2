# try,except and finally
# file

import os
try:
    full_path = os.getcwd() # get current working directory path
    full_path_file = full_path + "/Nirmal.txt"
    print(full_path_file)
    file = open('Nirmal.txt','r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("File is not found, fix the path or create the file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
