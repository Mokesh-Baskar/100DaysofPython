#lets create a leap year calc program where system outputs whether the year is leap or not

# rules are simple the year must be divisible by 4 , if the year divisible by 100 it must be divisible by 400 as well

#eg:2000 is leap year , 2100 is not a leap year

def leapyearcalc(year):

    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False    
    


userinput = int(input("Please input the year to check : "))

result = bool(leapyearcalc(userinput))

if result == True:
    print(" This year is a leap year")
else:
    print(" This year is not a leap year")