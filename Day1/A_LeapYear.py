x = int(input())

leap_year = False
days_feb = 0

if x % 4 == 0 and x % 100 != 0:
    leap_year = True
    days_feb = 29
elif x % 400 == 0:
    leap_year = True
    days_feb = 29
else:
    days_feb = 28

print(days_feb)