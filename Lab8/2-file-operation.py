# Write a program to write the integer numbers from 1 to 20 in a file called “NUMBER.txt”. Copy the contents of the file into two files “EVEN” and “ODD” so that even numbers will the in the “EVEN” file and odd number will be in the “ODD” file. Display the contents of all the files.

f1 = open("NUMBER.txt", "a+")  # open the file NUMBER.txt in append mode
for i in range(1, 21):
    f1.write(str(i) + " ")

f1 = open("NUMBER.txt", "r")  # open the file NUMBER.txt in read mode
numbers = f1.read()
numbers = numbers.split(sep=" ")
# print(numbers)

f2 = open("EVEN.txt", "a+")
f3 = open("ODD.txt", "a+")
for number in numbers:
    try:
        if int(number) % 2 == 0:
            f2.write(number + " ")
        else:
            f3.write(number + " ")
    except:
        continue

# Displaying the contents of each file
f1 = open("NUMBER.txt", "r")
f2 = open("EVEN.txt", "r")
f3 = open("ODD.txt", "r")

f1_text = f1.read()
f2_text = f2.read()
f3_text = f3.read()

print("Contents of NUMBER.txt", f1_text)
print("Contents of EVEN.txt", f2_text)
print("Contents of ODD.txt", f3_text)
