print("Are you a superfan of the series 'Dexter'?'")
print("Let's find out!")

killer = input("Who is the Bay Harbor butcher?")

if killer == "Dexter Morgan":
    print("Correct! You are a superfan!")
    print("Let's see how much you know about Dexter!")
    first_kill = input("Who was Dexter's first kill?")
    if first_kill == "Nurse Mary":
        print("Correct! You are a superfan!")
    else:
        print("Incorrect! You were so near!")
elif killer == "James Doakes":
    print("Wrong! But it seems you are familiar with the series!")
else:
    print("Wrong! You are not a fan!")
