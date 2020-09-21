y = int(input("enter year: "))
if (y % 4) == 0 & (y % 100) != 0 or (y % 400) == 0:
    print("%s is a leap year" %y)
else:
    print("%s is a NOT leap year" %y)
