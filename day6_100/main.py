print("Hello User!")
print()
print("Please login to continue")
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "Jake" and password == "jake1234":
    print("Welcome Jake!")
elif username == "Sarah" and password == "sarah1234":
    print("Welcome Sarah!")
elif username == "John" and password == "john1234":
    print("Welcome John!")
else:
    print("Who are you?")
