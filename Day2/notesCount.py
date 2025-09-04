def count(amount):
    if amount==0:
        return "no notes"
    count =0
    if amount>=2000:
        notes = amount//2000
        amount = amount-2000*notes
        count =count+ notes
    if amount>=500:
        notes = amount//500
        amount = amount-500*notes
        count += notes
    if amount>=200:
        notes = amount//200
        amount = amount-200*notes
        count+=notes
    if amount>=100:
        notes = amount//100
        amount = amount-100*notes
        count+=notes
    if amount>=50:
        notes = amount//50
        amount= amount-50*notes
        count+=notes
    if amount>=20:
        notes = amount//20
        amount= amount-20*notes
        count+=notes
    if amount>=10:
        notes = amount//10
        amount= amount-10*notes
        count+=notes
    if amount>=5:
        notes = amount//5
        amount= amount-5*notes
        count+=notes
    if amount>=2:
        notes = amount//2
        amount= amount-2*notes
        count+=notes
    if amount>=1:
        notes = amount//1
        amount= amount-1*notes
        count+=notes
    return count
amt = int(input("ENter amount: "))
print("Notes: ",count(amt))
        