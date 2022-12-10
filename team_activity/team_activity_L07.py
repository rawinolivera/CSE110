import random
magic_num = random.randint(1, 100)

# magic_num = int(input("Wat is the magic number? "))

# if magic_num > guess_num:
#     print("Higher")
# elif magic_num < guess_num:
#     print("Lower")
# else:
#         print("You guessed it!")

# while magic_num != guess_num:
#     if magic_num > guess_num:
#         print("Higher")
#         guess_num = int(input("What is your guess? "))
#     elif magic_num < guess_num:
#         print("Lower")
#         guess_num = int(input("What is your guess? "))

# print("You guessed it!")
answer = 'yes'
while answer.lower() == 'yes':
    track_num = 0
    magic_num = random.randint(1, 100)
    guess_num = int(input("What is your guess? "))
    while magic_num != guess_num:
        track_num = track_num + 1
        if magic_num > guess_num:
            print("Higher")
            guess_num = int(input("What is your guess? "))
        elif magic_num < guess_num:
            print("Lower")
            guess_num = int(input("What is your guess? "))

    print("You guessed it!")
    print(f"You tried {track_num} times!")
    answer = input("Do you want to play again? yes/no: ")

print("Game over!")