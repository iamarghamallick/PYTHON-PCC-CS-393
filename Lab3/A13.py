# The program takes two strings and displays which letters are in the first string but not in the second string.

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
for letter in s1:
    if letter not in s2:
        print(letter)