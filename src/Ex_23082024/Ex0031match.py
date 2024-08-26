user_type = input("Enter the user type,manager,admin, guest\n")
user_type = user_type.lower()
match user_type:
    case  "admin" | "manager":
        print("Hello Sir")
    case "guest":
        print("Hi Sir")
    case _:
        print("Hello There")