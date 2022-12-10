things = []
thing = ''
print("Please enter the items of the shopping list (type: quit to finish): ")
while thing != 'quit':
    thing = input("Item: ")
    if thing != 'quit':
        things.append(thing)
print()
print("The shopping list is:")
for thing in things:
    print(thing)
print()

print("The shopping list with indexes is:")
for i in range(len(things)):
    thing = things[i]
    print(f"{i}. {thing}")
print()

i = int(input("Which item would you like to change? "))
new_thing = input("What is the new item? ")
things[i] = new_thing
print()
print("The shopping list with indexes is:")
for i in range(len(things)):
    thing = things[i]
    print(f"{i}. {thing}")