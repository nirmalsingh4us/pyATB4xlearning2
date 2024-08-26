# syntax of match
# Match variable :
#   case pattern1:
# code block
# Case pattern2:
# Code block
# Write a program to ask the user which browser to run automation
browser_name = input("enter the name of browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name == "firefox":
            print("Hello")
        print("Execute the Firefox code")
    case "edge":
        print("Execute the Edge code")
    case"safari":
        print("Execute the Safari code")
    case _:
        print("Not found")