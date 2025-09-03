cname = input("Enter customer name: ")
cno = int(input("Enter customer number: "))
pmr = int(input("Enter present month reading: "))
lmr = int(input("Enter last month reading: "))
totalUnits = pmr-lmr
currBill = totalUnits*3.80
print("Consumer Details: ")
print("Consumer number: ",cno,"\nConsumer name: ",cname,"\nTotal current Bill: ",currBill)