from datetime import datetime

for _ in range(int(input())):
    t1, t2 = map(int, input().split())
    dt1 = datetime(2000, 1, 1, t1 // 100, t1 % 100)
    day2 = 2 if t2 < t1 else 1
    dt2 = datetime(2000, 1, day2, t2 // 100, t2 % 100)

    timespan = dt2 - dt1
    total_seconds = int(timespan.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    print(f"{hours} {'hour' if hours == 1 else 'hours'} {minutes} {'minute' if minutes == 1 else 'minutes'}")
