# Write a program to create, append, and remove lists in python

# create
list = []

# append
def append(v):
    return list.append(v)

# remove
def remove(v):
    return list.remove(v)

while(True):
    choise = int(input("Press 1 for Append, Press 2 for remove, Press 0 to exit\n"))
    if choise == 1:
        v = int(input("Enter value to be added: "))
        append(v)
        print(list)
    elif choise == 2:
        v = int(input("Enter the element to be removed: "))
        remove(v)
        print(list)
    elif choise == 0:
        exit()
    else:
        print("Try with valid input next time!")