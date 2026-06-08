# Creativity Addition: Added an input validation while loop at the beginning to
# ensure that the year of interest is within the range of the historical data.

interest_year = int(input("Enter year of interest: "))

while interest_year < 1751 or interest_year > 2019:
    print("Invalid interest year, please enter a year between 1751 and 2019.")
    interest_year = int(input("Enter year of interest: "))

lowest_expectancy = float("inf")
highest_expectancy = -1
lowest_country = ""
lowest_year = 0
highest_country = ""
highest_year = 0

year_total = 0
year_count = 0
year_min = float("inf")
year_max = -1
year_min_country = ""
year_max_country = ""

with open("life_expectancy.csv") as life_expectancy:
    next(life_expectancy)

    for line in life_expectancy:
        parts = line.strip().split(",")

        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life = float(parts[3])

        if life < lowest_expectancy:
            lowest_expectancy = life
            lowest_country = country
            lowest_year = year

        if life > highest_expectancy:
            highest_expectancy = life
            highest_country = country
            highest_year = year
    
        if year == interest_year:
            year_total += life
            year_count += 1

            if life < year_min:
                year_min = life
                year_min_country = country
            
            if life > year_max:
                year_max = life
                year_max_country = country

    average = year_total/year_count

    print()
    print(f"The overall max life expectancy is: {highest_expectancy} from {highest_country} in {highest_year}")
    print(f"The overall min life expectancy is: {lowest_expectancy} from {lowest_country} in {lowest_year}")
    print()
    print(f"For the year {interest_year}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max:.3f}")
    print(f"The min life expectancy was in {year_min_country} with {year_min:.3f}")