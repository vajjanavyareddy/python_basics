# You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
# 1.Add a product to the cart.
# 2.Remove a product from the cart 
# 3.Search for a product in the cart 
# 4.Display all products in the cart
# 5.Show the total number of products in the cart
 
# Cart Operations:
# 1. Add Product
# 2. Remove Product
# 3. Search Product
# 4. Display Cart
# 5. Count Products
# 6. Exit
 
# Enter choice: 1
# Enter product to add: Laptop
# Product 'Laptop' added to cart.
 
# Enter choice: 1
# Enter product to add: Phone
# Product 'Phone' added to cart.
 
# Enter choice: 4
# Cart: ['Laptop', 'Phone']
 
# Enter choice: 3
# Enter product to search: Phone
# Yes, 'Phone' is in the cart.
 
# Enter choice: 5
# Total products in cart: 2
li=[]
def ad(prod):
    
    li.append(prod)
def rem(prod):
    li.remove(prod)
def search(prod):
    for p in li:
        if p==prod:
            print(f"Element found. The prod is : {p}")
            return
    print("Element not found")
def display():
    print("The products are: ",li)
def total():
    print("No. of items: ",len(li))
def sortItems(li):
    li.sort()
    print("The sorted list is: ",li)
def clearItems(li):
    li.clear()
    print("The list is: ",li)
c = 0
print("1.Add product\n2.Remove product\n3.Search product\n4.Display products\n5.Total no. of products\n6.Sort list items\n7.Clear list items")
while(c<=7):
    c = int(input("Enter choice: "))
    if c==1:
        p=input("Enter product to add: ")
        ad(p)
    elif c==2:
        p=input("Enter prod to remove: ")
        rem(p)
    elif c==3:
        p=input("Enter search prod: ")
        search(p)
    elif c==4:
        display()
    elif c==5:
        total()
    elif c==6:
        sortItems(li)
    elif c==7:
        clearItems(li)
    else:
        print("Invalid choice")

    