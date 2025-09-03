def leapYear(year):
    if   year % 4==0 and (year % 400 == 0 or year%100 !=0):
        return "leap year"
   
    else:
        return "not a leap year"
year = int(input("Enter year: "))
print("Given year is ",leapYear(year))