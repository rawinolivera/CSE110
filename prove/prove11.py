with open("../life-expectancy.csv") as life_expectancy_data:
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

    highest_exp = 0.00
    lowest_exp = 999999999.99
    
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

        if life_exp[i] > highest_exp:
            highest_exp = life_exp[i]
            ge_hi_year = year[i]
            ge_hi_entity = entity[i]

        if life_exp[i] < lowest_exp:
            lowest_exp = life_exp[i]
            ge_lo_year = year[i]
            ge_lo_entity = entity[i]

    print(f"The overall max life expectancy is: {highest_exp}")
    print(f"The overall min life expectancy is: {lowest_exp}")
    print()