secret_word = 'mosiah'
guess_time = 0
guess_word = ''
print("Welcome to the word guessing game!")
print()
times = int(input("How many chances do you need to play? "))
while guess_time < times and secret_word != guess_word:
    
    chances = times - guess_time
    if chances == 1:
        print("***This is your last chance***")

    guess_word = input("What is your guess? ")
    guess_word = guess_word.lower()
    secret_word = secret_word.lower()
    if guess_word != secret_word:
        if len(guess_word) != len(secret_word):
            print("Sorry, the len must have the same number of letters")
        else:
            print("Your hint is: ")
            for i, letter in enumerate(guess_word): # b l o w
                new = 0
                for j, hint in enumerate(secret_word):  # w o r d 
                    if hint == letter:
                        if j == i:
                            #print(letter.upper(), end="#")
                            if new < 2:
                                new = 2
                        else:
                            #print(letter, end="#")
                            if new < 1:
                                new = 1              
                if new == 0:
                    print("_", end=" ")
                elif new == 1:
                    print(letter, end=" ")
                elif new == 2:
                    print(letter.upper(), end=" ")       
            print()
    guess_time = guess_time + 1

if guess_time == times and secret_word != guess_word:
    print("That was your last chance")
    print("Game Over!")
else:
    print("Congratulations! You guessed it!")
    print(f"It took you {guess_time} guesses.")