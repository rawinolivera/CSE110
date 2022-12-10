
print("Enter a list of numbers, type 0 when finished.")
numbers = []
sorted_numbers = []

data = -1
while data != 0:
    data = int(input("Enter number: "))
    if data != 0:
        numbers.append(data)
print(numbers)

total_numbers = 0
average = 0
largest_number = 0
smallest_num = 1000000000000000
count = 0
for number in numbers:
    total_numbers += number
    if number > largest_number:
        largest_number = number
    if number > 0 and number < smallest_num:
        smallest_num = number

sorted_numbers = sorted(numbers)
count = len(numbers)
average = total_numbers / count

print(f"The sum is: {total_numbers}")
print(f"The average is: {average}")
print(f"The largest number is: {largest_number}")
print(f"The smallest number is: {smallest_num}")
for element in sorted_numbers:
    print(element)