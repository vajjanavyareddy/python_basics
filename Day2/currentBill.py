def bill(tu):
    if tu>=1 and tu<=50:
        return tu*3.80
    elif tu>50 and tu<=100:
        return 50*3.80+(tu-50)*4.20
    elif tu>100 and tu<=200:
        50*3.80+50*4.20+(tu-100)*5.10
    elif tu>200 and tu<=300:
        50*3.80+50*4.20+100*5.10+(tu-200)*6.30
    else:
        50*3.80+50*4.20+100*5.10+100*6.30+(tu-300)*7.50
cname = input("Enter customer name: ")
cno = int(input("Enter customer number: "))
pmr = int(input("Enter present month reading: "))
lmr = int(input("Enter last month reading: "))
totalUnits = pmr-lmr
print("Consumer Details: ")
print("Consumer number: ",cno,"\nConsumer name: ",cname,"\nTotal current Bill: ",bill(totalUnits))