try:
    with open("NS_TEST/NS.txt", 'r') as file:
        content = file.readlines()
    print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    try:
        file.close()
    except NameError as ne:
        print("ne")
