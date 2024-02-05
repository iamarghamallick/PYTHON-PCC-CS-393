# 3. Write a program to reverse a List(without using reverse function)

def reverse(lst):
    rev_lst = []
    for n in lst:
        rev_lst.insert(0, n)
    return rev_lst

print(reverse([1,2,3,4,5]))