with open("life-expectancy.csv") as life_expectancy_data:
    str_entity = []
    str_entity2 = []
    str_code = []
    str_year = [] #str
    str_life_exp = []  #str
    entity = []
    code = []
    year = []
    life_exp = []
    for i in life_expectancy_data:
        
        #eliminate extra lines and spaces
        i = i.strip()
        #separate the elements among the space
        i = i.split(",")

        str_entity.append(i[0])
        if i[0][0] == '"':
            str_entity2.append(i[1])
            str_code.append(i[2])
            str_year.append(i[3])
            str_life_exp.append(i[4])
        else:
            str_entity2.append('')
            str_code.append(i[1])
            str_year.append(i[2])
            str_life_exp.append(i[3])    

    total_year_quantity = 0
    highest_exp = 0.00
    lowest_exp = 999999999.99
    highest_exp2 = 0.00
    lowest_exp2 = 999999999.99
    average = 0.00
    hi_year = ''
    hi_entity = ''
    lo_year = ''
    lo_entity = ''
    hi_year2 = ''
    hi_entity2 = ''
    lo_year2 = ''
    lo_entity2 = ''
    ge_highest_exp = 0.00
    ge_lowest_exp = 999999999.99
    ge_average = 0.00
    ge_hi_year = ''
    ge_hi_entity = ''
    ge_lo_year = ''
    ge_lo_entity = ''
    total_years = 0
    total_exp = 0
    total_exp2 = 0
    interested_year = input("Enter the year of interest: ")
    interested_country = input("Enter the country of interest: ")
    print()

    for i in range(1, len(str_life_exp)):
        life_exp.append(float(str_life_exp[i]))
        if str_entity[i][0] == '"':
            entity.append(str_entity[i] + ',' + str_entity2[i])
        else:
            entity.append(str_entity[i])
        code.append(str_code[i])
        year.append(str_year[i])

    for i in range(0, len(entity)):

        if life_exp[i] > ge_highest_exp:
            ge_highest_exp = life_exp[i]
            ge_hi_year = year[i]
            ge_hi_entity = entity[i]

        if life_exp[i] < ge_lowest_exp:
            ge_lowest_exp = life_exp[i]
            ge_lo_year = year[i]
            ge_lo_entity = entity[i]

        if  year[i] == interested_year:
            total_year_quantity += 1
            total_exp += life_exp[i]
            if life_exp[i] > highest_exp:
                highest_exp = life_exp[i]
                hi_year = year[i]
                hi_entity = entity[i]

            if life_exp[i] < lowest_exp:
                lowest_exp = life_exp[i]
                lo_year = year[i]
                lo_entity = entity[i]
        

        country = entity[i]
        if  country.lower() == interested_country.lower():
            total_exp2 = total_exp2 + life_exp[i]
            total_years = total_years + 1
            new_country = entity[i]
            if life_exp[i] > highest_exp2:
                highest_exp2 = life_exp[i]
                hi_year2 = year[i]

            if life_exp[i] < lowest_exp2:
                lowest_exp2 = life_exp[i]
                lo_year2 = year[i]
        
    average = total_exp / total_year_quantity
    average2 = total_exp2 / total_years
    print()

    print(f"The overall max life expectancy is: {ge_highest_exp} from {ge_hi_entity} in {ge_hi_year}")
    print(f"The overall min life expectancy is: {ge_lowest_exp} from {ge_lo_entity} in {ge_lo_year}")
    print()
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The overall max expectancy was in {hi_entity}  {highest_exp} ")
    print(f"The overall min expectancy was in {lo_entity} with {lowest_exp}")
    print()

    print(f"The overall max life expectancy is: {highest_exp2} from {new_country} in {hi_year2}")
    print(f"The overall min life expectancy is: {lowest_exp2} from {new_country} in {lo_year2}")

    print(f"The average life expectancy across all years was {average2:.2f}")
