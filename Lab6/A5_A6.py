# 5.A) Using function, write a program to input n numbers into a list and arrange the numbers in descending order using Bubble sort technique.

# 5.B) Accept another number(P) to search the sorted list using linear search algorithm. If the search element is present in the list then print “Search successful else print “Search unsuccessful”.

# 6. Using question No. 5(A): Accept another number(P) to search the sorted list using binary search algorithm. If the search element is present in the list then print “Search successful” else print “Search unsuccessful”.

def bubble_sort_descending(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def linear_search(lst, p):
    for n in lst:
        if n == p:
            print("Search Successful")
            return
    print("Search Unsuccessful")


def binary_search(sorted_lst, p):
    first = 0
    last = len(sorted_lst)-1
    while first <= last:
        mid = (first+last) // 2
        if sorted_lst[mid] == p:
            print("Search Successful")
            return
        elif sorted_lst[mid] < p:
            last = mid-1
        else:
            first = mid+1
    print("Search Unsuccesful")

def main():
    lst = []
    n = int(input("Enter the number of elements: "))
    for _ in range(n):
        lst.append(int(input("Enter number: ")))

    sorted_lst = bubble_sort_descending(lst)
    print("Sorted in Descending Order:", sorted_lst)

    p = int(input("Enter the element to search (using linear search): "))
    linear_search(lst, p)

    p = int(input("Enter the element to search (using binary search): "))
    binary_search(sorted_lst, p)

if __name__ == "__main__":
    main()