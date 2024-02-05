# Write a program to implement random access in a file.

"""
Function details
1. tell() -> returns the current file position in a file stream.
2. seek(n) -> change the file position to n-th
3. read() -> reads and returns the whole file content as string
4. read(n) -> reads and returns first n bytes of the file
"""

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
