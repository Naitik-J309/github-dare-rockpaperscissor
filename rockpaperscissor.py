import random
fun_dares = [
    "Talk in an accent for the next 3 rounds",
    "Do your best celebrity impression until someone guesses who it is",
    "Try to lick your elbow",
    "Speak without using the letter 'E' for one minute",
    "Pretend you're a cat for 2 minutes",
    "Sing the chorus of your favorite song out loud",
    "Do your best runway walk across the room",
    "Call a friend and confess your love for a fictional character",
    "Recite the alphabet backwards",
    "Serenade the person to your left like you’re in a rom-com",
    "Type a random emoji and post it on your Instagram story",
    "Send 'I'm watching you...' to the 3rd contact in your phone",
    "Text your crush 'We need to talk...' then say 'jk dare 😅'",
    "Change your profile name to something ridiculous for 10 minutes",
    "Scroll through your camera roll blindfolded and post the first photo you land on",
    "Make up a story using 3 random words the group gives you",
    "Pretend to be a news anchor and deliver breaking news about something mundane",
    "Balance a book on your head and walk in a straight line",
    "Draw a self-portrait blindfolded",
    "Do 10 push-ups while making animal sounds",
    "Act like a grandma/grandpa telling a story from 'the good old days'",
    "Try to juggle with random soft objects nearby",
    "Give a dramatic Oscar-worthy speech about your favorite snack",
    "Speak in rhymes only for the next two turns",
    "Let the group write a message and send it to someone in your contacts"
]
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          ROCK
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
           PAPER
""")
scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          SCISSOR
""")
playable = [rock,paper,scissor]
pc=0
cc=0
playerchoice = input("Enter rock, paper, or scissor: ")
if playerchoice=="rock":
    pc=1
    print(rock)
elif playerchoice=="paper":
    pc=2
    print(paper)
elif playerchoice=="scissor":
    pc=3
    print(scissor)
else:
    print("Please give a proper choice.")
    exit()
computerchoice=random.choice(playable)
cc=playable.index(computerchoice)+1
print("Computer chose",computerchoice)
if pc==cc:
    print("Its a draw")
elif pc==1 and cc==3:
    print("You win!")
elif pc==3 and cc==1:
    print("You lose!")
    print("A dare for you: ",random.choice(fun_dares))
elif pc>cc:
    print("You win!")
else:
    print("You lose")
    print("A dare for you: ",random.choice(fun_dares))

    