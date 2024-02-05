'''
A14. Python program to Sort a List of Tuples in Increasing Order by the Second element in Each Tuple.
Input:
list of tuples: (2,30,6),(10,6,9)(20,25,40,100)
Output:
List of tuples: (10,6,9),(20,25,40,100),(2,30,6)
Explanation:
2nd elements are 30,6,25 in output. If we arrange them in ascending order it will be 6,25,30
'''

lst = [(2,30,6),(10,6,9),(20,25,40,100)]
sorted_lst = sorted(lst, key=lambda x: x[1])
print(sorted_lst)