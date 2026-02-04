



# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes



def tell_joke(setup, joked):
    input("Knock Knock ")
    input(setup)
    print(joked)
    again = input("Do you want to hear another joke or are you finished? ")
    if again == "finished":
        finished()



def finished():
    num = int(input("Please rate our game 1-10! "))
    final_score = int(num * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")

name = input("Please enter your name: ")

jokes = [
    {"name": "robber", "setup": "Calder ", "joked": "Calder police - I've been robbed!"},
    {"name": "tank", "setup": "Tank", "joked": "You are welcome!"},
    {"name": "pencil", "setup": "Broken pencil", "joked": "Nevermind, it's pointless!"},
]




def choose_jokes(jokes):
    while True:
        print("\nAvailable joke types:")
        for j in jokes:
            print("- " + j['name'])
        question = input("Which type would you like? ").strip().lower()
        if question == 'none':
            print("Goodbye!")
            break
        selected = next((j for j in jokes if j['name'] == question), None)
        if selected:
            tell_joke(selected['setup'], selected['joked'])
            again = input("Hear another? (yes/no) ").strip().lower()
            if again != 'yes':
                break
        else:
            print("Sorry, I didn't recognize that choice.")
    finished()


start = input("Do you want to hear a joke? ")
if start.strip().lower() == "no":
    print("Okay suit yourself!")
elif start.strip().lower() == "yes":
    print("Great, Let's Play")
    choose_jokes(jokes)
else:
    finished()




def end(name):
    print("Thank you for playing, " + name + "!")
    exit()

end(name)
