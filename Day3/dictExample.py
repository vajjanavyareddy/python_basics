# You are building a Library Management System in Python. The system should store books in a dictionary where:
# Key → Book ID
# Value → Book Title
# Write a Python program to perform the following operations using Dictionaries:
# Add a book to the library (Book ID, Title).
# Remove a book using Book ID.
# Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# Count the total number of books in the library.
# Check if a book title exists in the library (reverse lookup).
dict1={}
def addBook(key,value):
    dict1[key]=value
def delBook(key):
    if key in dict1:
        removed = dict1.pop(key)
        print(f"removed: {removed}")
    else:
        print("Book id not found")
    
def search(value):
    for b_key,b_value in dict1.items():
        if b_value.lower()==value.lower():
            print("Book found")
            return
            
    print("Book not found")
def update(key,value,dict1):
    if key in dict1:
        dict1[key]=value
        print("updated")
    else:
        print("not found")
def display():
    print(dict1)

def count():
   print("Total Books: ",len(dict1))
c=0

print("1.Add Book\n2.Delete Book\n3.Search Book\n4.Update Book\n5.Display\n6.Count")
while(True):
    c = int(input("Enter choice: "))
    if c==1:
        key=input("Enter id: ")
        value = input("Enter book title")
        addBook(key,value)
    elif c==2:
        key = input("book id to delete: ")
        delBook(key)
    elif c==3:
        title = input("Enter title to search")
        search(title)
        
    elif c==4:
        key = input("Enter book id to change title: ")
        value = input("Enter title to change: ")
        update(key,value,dict1)
    elif c==5:
        display()
    elif c==6:
        count()
    elif c==0:
        print("Exiting")
        break
    else:
        print("Invalid choice")
