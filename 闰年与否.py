years = input()
years = int(years)
LeapYear = years % 4
if LeapYear == 0:
    print("Yes")
else:
    print("No")
