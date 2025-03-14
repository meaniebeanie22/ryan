MONTH_DAY = {
    "january": 0,
    "february": 31,
    "march": 59,
    "april": 90,
    "may": 120,
    "june": 151,
    "july": 181,
    "august": 212,
    "september": 243,
    "october": 273,
    "november": 304,
    "december": 334,
}
month, day = input("Month: ").lower(), int(input("Day: "))
try:
    day_of_year = MONTH_DAY[month] + day
except KeyError:
    print("Invalid month entered")

if day_of_year >= 335 or day_of_year < 79:
    print("Summer")
elif day_of_year <= 171:
    print("Autumn")
elif day_of_year <= 264:
    print("Winter")
else:
    print("Spring")
