
print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name? ")
name_lower = name.lower()


if name_lower == "mark":
    DOW = input("What is the day of the week? ")
    DOW_lower = DOW.lower()
    if DOW_lower == "monday":
        print("It is going to be a great Monday", name)
    if DOW_lower == "tuesday":
        print("What a wonderful Tuesday it is", name)
    if DOW_lower == "wednesday":
        print("Happy Hump Day", name)
    if DOW_lower == "thursday":
        print(name, "your week is almost over!")
    if DOW_lower == "friday":
        print(name, "It's FRIDAY!")

elif name_lower == "david":
    DOW = input("What is the day of the week? ")
    DOW_lower = DOW.lower()
    if DOW_lower == "monday":
        print("It is going to be a great Monday", name)
    if DOW_lower == "tuesday":
        print("You look great in that color", name)
    if DOW_lower == "wednesday":
        print("You look chipper today", name)
    if DOW_lower == "thursday":
        print(name, "you are doing a great job!")
    if DOW_lower == "friday":
        print(name, "it's FRIDAY!")
    else:
        print(
            "I do not know your name, but I hope you are having a great day!"
            )
