# Write a Python Program to find the union of two lists.

lst1 = [10,20,30,40,30,50,60]
lst2 = [10,15,20,30,25,25]
lstU = list(set(lst1) | set(lst2))
print(lstU)