# You are asked to design a simple Payment System that can handle different payment methods.
# Requirements:
# Create a base class Payment with a method pay(amount).
# Create three child classes that override the pay(amount) method:
# CashPayment → print "Paid ₹<amount> in cash"
# CardPayment → print "Paid ₹<amount> using credit/debit card"
# UPIPayment → print "Paid ₹<amount> using UPI"
# Task:
# Create a list of payment objects (CashPayment, CardPayment, UPIPayment).
# Loop through them and call pay(1000).
# Each object should print a different message.
class Payment:
    def pay(self):
       pass
class Cashpayment(Payment):
    def pay(self,amount):
        print(f"Cash Payment {amount} is done")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"Card Payment {amount} is done")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"UPI Payment {amount} done")
cash = Cashpayment()
card = CardPayment()
upi = UPIPayment()
payments = [cash,card,upi]
for p in payments:
    p.pay(1000)