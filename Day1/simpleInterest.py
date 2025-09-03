#Simple interest calculation
amount = int(input("Enter amount\n"))
time = int(input("ENter no. of months\n"))
rate = int(input("Enter rate\n"))
intrest = (amount*time*rate)/100
totalAmount= amount+intrest
print("Interest: ",intrest)
print("Total Amount: ",totalAmount)