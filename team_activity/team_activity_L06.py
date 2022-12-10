# fir_rider_age = float(input("What is the age of the first rider? "))
# fir_rider_height = float(input("What is the height of the first rider? "))
# sec_rider = input("Is there a second rider (yes/no)? ")
# if sec_rider.lower() == 'yes':
#     sec_rider_age = float(input("What is the age of the second rider? "))
#     sec_rider_height = float(input("What is the height of the second rider? "))
#     if (fir_rider_age >= 18 or sec_rider_age >= 18) and fir_rider_height >= 36 and sec_rider_height >= 36:
#         ride_acceptable = True
#     else:
#         ride_acceptable = False

# else:
#     if fir_rider_age >= 18 and fir_rider_height >= 36:
#         ride_acceptable = True
#     else:
#         ride_acceptable = False

fir_rider_age = float(input("What is the age of the first rider? "))
fir_rider_height = float(input("What is the height of the first rider? "))
if fir_rider_age >= 12 and fir_rider_age < 18:
    fir_rider_gold_p = input("Do you have a Golden Pasport (yes/no): ")
sec_rider = input("Is there a second rider (yes/no)? ")
if sec_rider.lower() == 'yes':
    sec_rider_age = float(input("What is the age of the second rider? "))
    sec_rider_height = float(input("What is the height of the second rider? ")) 
    if sec_rider_age >= 12 and fir_rider_age < 18:
        sec_rider_gold_p = input("Do you have a Golden Pasport (yes/no): ")

    if (fir_rider_gold_p.lower() == 'yes' or sec_rider_gold_p.lower() == 'yes') and (fir_rider_height >= 36 or sec_rider_height >= 36): 
            ride_acceptable = True
    elif (fir_rider_age >= 18 or sec_rider_age >= 18) and (fir_rider_height >= 36 and sec_rider_height >= 36):
        ride_acceptable = True
    elif (fir_rider_age >= 14 and sec_rider_age >= 16) or (fir_rider_age >= 16 or sec_rider_age >= 14) and (fir_rider_height >= 36 and sec_rider_height >= 36):
        ride_acceptable = True
    elif (fir_rider_age >= 12 and sec_rider_age >= 12) and fir_rider_height >= 52 and sec_rider_height >= 52:
        ride_acceptable = True
    else:
        ride_acceptable = False

else:
    if fir_rider_gold_p.lower() == 'yes' and fir_rider_height >= 36:
            ride_acceptable = True
    elif fir_rider_age >= 18 and fir_rider_height >= 36:
        ride_acceptable = True
    else:
        ride_acceptable = False

if ride_acceptable:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")