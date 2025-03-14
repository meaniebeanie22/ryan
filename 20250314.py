MONTH_DAY = {
    "january": (0, 31),
    "february": (31, 28),
    "march": (59, 31),
    "april": (90, 30),
    "may": (120, 31),
    "june": (151, 30),
    "july": (181, 31),
    "august": (212, 31),
    "september": (243, 30),
    "october": (273, 31),
    "november": (304, 30),
    "december": (334, 31),
}
month, day = input("Month: ").lower(), int(input("Day: "))
if not 0 < day <= MONTH_DAY[month][1]:
    print("Invalid")
    exit()
try:
    day_of_year = MONTH_DAY[month][0] + day
except KeyError:
    print("Invalid")

if day_of_year >= 335 or day_of_year < 79:
    print("Summer")
elif day_of_year <= 171:
    print("Autumn")
elif day_of_year <= 264:
    print("Winter")
else:
    print("Spring")
