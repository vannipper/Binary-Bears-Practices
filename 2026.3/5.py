from datetime import datetime

def get_suffix(n):
    if 11 <= (n % 100) <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

for _ in range(int(input())):
    dateStr = input()
    dt = datetime.strptime(dateStr, "%m/%d/%Y")
    day_of_year = int(dt.strftime("%j"))

    print(f"{dateStr} is a {dt.strftime("%A")} and the {day_of_year}{get_suffix(day_of_year)} day of the year.")
