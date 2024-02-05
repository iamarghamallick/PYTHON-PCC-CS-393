# Python program to remove an empty element from a list.

num = ["Hello", 34, 45, "", 40, ""]
for i in num:
    if i == "":
        num.remove("")

print(num)