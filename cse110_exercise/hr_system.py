#Human Resource Management System

with open("/Users/moses/Desktop/BYU School/CSE 110 - PYTHON/introduction_to_programmin_CSE110/cse110_exercise/hr_system.txt") as data_system:
    #The file has been open and store in variable "data_system"

    #Skip the header which is first line
    next(data_system)
    #Read each line, one by one, into a variable: current_line

    for line in data_system:
        #strip off leading/training whitespace.
        #This is important, otherwise, our last will have \n character with it.
        current_line = line.strip()

        #Split the current_line into parts base on a space " " as the seperator
        parts = current_line.split()
        
        #save each part into a variable

        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])
        # Output the data as desired
        # This would display for the basic requirement
        # print(f"{name} (ID: {id_number}), {title} - ${salary:.2f}")

        #Calculate the paycheck amount
        pay_amount = salary / 24
        
        #Compute engineering bonus
        if title.lower() == "engineer":
            pay_amount += 1000
        #Output the data as desire
        print(f"{name} (ID: {id_number}), {title} - ${pay_amount:.2f} ")
