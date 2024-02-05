# Write a program to count number of words in a sentence.
s = input("Enter a sentence: ")
count = 0
for word in s.split(sep=" "):
    count = count + 1

print("Total number of words in your sentence is", count)