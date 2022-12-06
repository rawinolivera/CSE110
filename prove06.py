#Milestone Adventure Game
user_name = input("What's your name: ")
print()
print(f"Hello {user_name}!!")
print("You're so Welcome to Milestone Game!")
print("In this adventure you are the one who chooses the end of the story")
print()
choice = input("You are walking on a high mountain and find two items: a ROPE and a BINOCULARS. Which one do you want to pick up? ")

if choice.lower() == 'rope':
    choice_a = input("You grab the rope and realized you can't see the other side of the rope, so after walking for a while following the rope, you find a cabin. Now, you are in front of the cabin door and have two options KNOCK or ENTER. What do you do? ")
    #new options:
    if choice_a.lower() == 'knock':
        choice_a_1 = input("You Knock the door, a kind voice invites you to come in and says that you can SLEEP or EAT. What do you chose? ")
        #last options:
        if choice_a_1.lower() == 'eat':
            print(f"Eatting helps the body to recover energy, good choice {user_name}!")
        elif choice_a_1.lower() == 'sleep':
            print(f"Sometimes we need some rest to continue with the adventure, good night {user_name}!")
        else:
            print("Your answer is not valid. Try again!") 

    elif choice_a.lower() == 'enter':
        choice_a_2 = input("Enter without knocking the door was not polite, you need to earn the right to serve of the house, first contribute with the cleanning of the house. Choose one article BROOM/MOP/VACUUM: ")
        if choice_a_2.lower() == 'broom':
            print(f"Sweepig the floor is a good start, Good Luck {user_name}!!")
        elif choice_a_2.lower() == 'mop':
            print(f"Mooping can be tired, but nothing feels better than a clean ground, do your best {user_name}!!")
        elif choice_a_2.lower() == 'vacuum':
            print(f"The vacuum will help saving you time, nice choice {user_name}!!")
        else:
            print("Your answer is not valid. Try again!") 

elif choice.lower() == 'binoculars':
    choice_b = input("You watch through the binoculars and see there is a flock of birds in your direction, they look hungry and aggresssive. What do you do now? HIDE or RUN: ")
    #new options:
    if choice_b.lower() == 'hide':
        choice_b_1 = input("You hide yourself behind a tree when you realize your feet are under the anthill. What do you do CLIMB the tree or FLEE away: ")
        if choice_b_1.lower() == 'climb':
            print(f"{user_name} Sometimes fate surprises us, On the tree you will enjoy the view of the birds comming!")
        elif choice_b_1.lower() == 'flee':
            print(f"{user_name}, saving your life looks like the best choice, but flock of birds are natural beautiful thing to see...")
        else:
            print("Your answer is not valid. Try again!") 

    elif choice_b.lower() == 'run':
        choice_b_2 = input("I've never seem someone down the mountain that fast... I will help you recover. What do you like LEMONADE or  WATER? ")
        if choice_b_2.lower() == 'lemonade':
            print("Vitamine C will power your body!")
        elif choice_b_2.lower() == 'water':
            print("Water is perfect to hydrate your body!!")
        else:
            print("Your answer is not valid. Try again!") 
else:
    print("Your answer is not valid. Try again!")    


