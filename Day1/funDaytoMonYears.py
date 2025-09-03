def convert(day):
    month = day/30
    year = day/365
    print("Months: ",round(month,2))
    print("Years: ",round(year,2))
    
days = int(input("Enter days: "))
convert(days)