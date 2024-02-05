# Write a program to implement random access in a file.

f = open("words.txt", "r")

print("Before reading File pointer position:", f.tell())
s = f.read()
print("After reading the file pointer position:", f.tell())
f.seek(0)
print("From the beginning of the file again", f.tell())
s = f.read(4)
print("First 4 bytes are:", s)
print("File pointer position:", f.tell())
s = f.read(3)
print("Next 3 bytes are:", s)
print("File pointer position:", f.tell())
f.close()