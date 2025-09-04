def week(num):
    if num==0: return "sunday"
    elif num==1: return "monday"
    elif num==2: return "tuesday"
    elif num==3: return "wednesday"
    elif num==4: return "thursday"
    elif num==5: return "friday"
    elif num==6: return "saturday"
    else:
        return "Invalid input"
num = int(input("Enter day: "))
print("Day is: ",week(num))
    