


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes



def robber():
    input("Knock Knock ")
    input("Calder")
    print("Calder police - I've been robbed!")
    joke = input("Do you want to hear another joke or are you finished? ")
    if joke == "finished":
        finished()


def tank():
    input("Knock Knock ")
    input("Tank ")
    print("You are welcome! ")
    joke = input("Do you want to hear another joke or are you finished? ")
    if joke == "finished":
        finished()

def pencil():
    input("Knock Knock ")
    input("Broken pencil ")
    print("Nevermind, it's pointless! ")
    joke = input("Do you want to hear another joke or are you finished? ")
    if joke == "finished":
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

jokes = ["robber", "tank", "pencil"]




joke = input("Do you want to hear a joke? ")
if joke == "no":
    print("Okay suit yourself!")
elif joke == "yes":
    print("Great, Let's Play")
    print("Available joke types:")
    for j in jokes:
        print("- " + j)
    question = input("Which type would you like? ('robber', 'tank', or 'pencil') ")
    if question == "robber":
        robber()
    elif question == "tank":
        tank()
    elif question == "pencil":
        pencil()
    else:
        print("Sorry, I didn't recognize that choice.")
else:
    finished()




def end(name):
    print("Thank you for playing, " + name + "!")
    exit()

end(name)

