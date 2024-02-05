r = int(input("Enter number of rows: "))

for i in range(r):
    for j in range(r-i):
        print("* ", end="")
    print("\r")
