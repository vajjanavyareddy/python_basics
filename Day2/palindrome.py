def palindrome(n):
    rev = reverse(n)
    if(n==rev):
        return "palindrome"
    else:
        return "not a palindrome"
def reverse(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
num=int(input("Enter number: "))
print("The given number is ",palindrome(num))
