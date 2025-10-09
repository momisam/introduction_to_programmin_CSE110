#Data Analysis for life expentancy 

with open("life-expectancy.csv") as file:
    next(file)
    for line in file:

        line = line.strip()

        parts = line.split(",")

        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])

        min_life = 9999
        max_life = 0

        if life_expectancy < min_life:
            min_life = life_expectancy

        if life_expectancy > max_life:
            max_life = life_expectancy

        print(f"Lowest life expectancy: {min_life}")
        print(f"Highest life expectancy: {max_life}")



