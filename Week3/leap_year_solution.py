yr = int(input("Please enter a year in the form 'yyyy'"))
    
if (yr > 999 and yr < 10000):
    if yr % 400 == 0:
        print("Year is a leap-year")
    elif yr % 100 == 0:
        print("Year is not a leap-year\n4 years since last leap year")   
    elif yr % 4 == 0:
        print("Year is a leap-year")        
    else:
        print("Year is not a leap-year")
        for i in range(1,4):
            if (yr - i) % 400 == 0:
                print(i, "years since leap year")
            elif (yr - i) % 100 == 0:
                print(i + 4, "years since leap year")
            elif (yr - i) % 4 == 0:
                print(i, "years since leap year")
else:
    print("You did not enter a valid year")
