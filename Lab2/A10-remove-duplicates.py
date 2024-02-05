# Write a program in Python to remove duplicate items from a list.

num = [2,3,4,5,2,6,3,2]

new_num = []

for i in num:
    if i not in new_num:
        new_num.append(i)

print(new_num)