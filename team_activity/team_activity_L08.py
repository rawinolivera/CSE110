# word = 'commitment'

# # for i, letter in enumerate(word):
# #     print(letter, end="")

# # print()
# fav_letter = input("What is your favorite letter? ")

# side = len(word)

# for i in range(side):
#     letter = word[i]
#     if letter == fav_letter:
#         letter = '_'
#     print(letter, end="")

# print()
answer = 'yes'

while answer == 'yes':
    quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
    num = int(input("Please enter a number: "))
    j = 0
    for i, letter in enumerate(quote):
        if i == j:
            letter = letter.upper()
            j = j + num
        print(letter, end="")
    print()
    answer = input("Would you like to enter another number? ")
print("Good Bye!")
