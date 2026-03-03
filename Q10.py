def days_since_birthday(birthday):
    """
    birthday format: "DD-MM-YYYY"
    returns number of days passed since birth,
    excluding birth year and current year
    """

    parts = birthday.split("-")
    birth_year = int(parts[2])

    current_year = 2026

    total_days = 0


    for year in range(birth_year + 1, current_year):
        total_days += 365


        if year % 4 == 0:
            if year % 100 != 0 or year % 400 == 0:
                total_days += 1

    return total_days



birthday_input = input("Enter your birthday in the format DD-MM-YYYY: ")

result = days_since_birthday(birthday_input)

print("Number of full days passed (excluding birth year and current year):", result)