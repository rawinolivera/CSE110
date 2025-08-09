# Calculate wind_chill (°F) given the temperature (Celsius or Farenheit)
def wind_chill(temp, grades_kind):
    # entries
    result = 0.00
    grades_kind = grades_kind.upper()
    if grades_kind == 'C':
        temp = temp * 1.8 + 32
    # computing
    result = 35.74 + .6215 * temp - 35.75 * (speed ** 0.16) + 0.4275 * temp * (speed ** 0.16)
    return result

temp = float(input("What is the temperature? "))
grades_kind = input("Fahrenheit or Celsius (F/C)? ")

for i in range(1, 13):
    speed = 5 * i
    result = wind_chill(temp, grades_kind)
    print(f"At temperature {temp}{grades_kind}, and wind speed {speed} mph, the windchill is: {result:.2f}{grades_kind}")