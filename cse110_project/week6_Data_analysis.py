#Data Analysis for life expentancy 

with open("life-expectancy.csv") as file:
    next(file)


    min_life = 9999
    max_life = 0

    min_country = ""
    min_year = ""
    max_country = ""
    max_year = ""

    all_data = []

    for line in file:
        line = line.strip()
        parts = line.split(",")
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        all_data.append([country, code, year, life_expectancy])

         #Check for lowest life expectancy
        if life_expectancy < min_life:
            min_life = life_expectancy
            min_country = country
            min_year = year

        # Check for highest life expectancy
        if life_expectancy > max_life:
            max_life = life_expectancy
            max_country = country
            max_year = year

        # After the loop, print overall results
print(f"The overall max life expectancy is: {max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")
print()


year_of_interest = int(input("Enter the year of interest: "))

# Create variables to find stats for that year
total_life = 0
count = 0
year_min = 9999
year_max = 0
year_min_country = ""
year_max_country = ""

# Go through all saved data again
for record in all_data:
    country = record[0]
    year = record[2]
    life = record[3]

    # Only look at rows matching the year entered
    if year == year_of_interest:
        total_life += life
        count += 1

        if life < year_min:
            year_min = life
            year_min_country = country

        if life > year_max:
            year_max = life
            year_max_country = country

# Compute average for that year
if count > 0:
    average_life = total_life / count

    # Show the results
    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average_life:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max:.2f}")
    print(f"The min life expectancy was in {year_min_country} with {year_min:.2f}")
else:
    print("No data found for that year.")
