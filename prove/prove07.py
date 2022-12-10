secret_word = 'mountain'
guess_time = 0
guess_word = ''
print("Welcome to the word guessing game!")
print()
while secret_word != guess_word:
    guess_time = guess_time + 1
    guess_word = input("What is your guess? ")
    guess_word = guess_word.lower()
    if guess_word != secret_word:
        print("Your guess was not correct.")

print("Congratulations! You guessed it!")
print(f"It took you {guess_time} guesses.")