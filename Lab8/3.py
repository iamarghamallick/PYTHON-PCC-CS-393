# To write a Python program to find the most frequent words in a text read from a file.

f = open("words.txt", "r")
text = f.read()
words = text.split(sep=" ")

d = {}
maxCount = 0
most_fre_word = ""
for word in words:
    if d.__contains__(word):
        d[word] = d[word] + 1
        if d[word] > maxCount:
            maxCount = d[word]
            most_fre_word = word
    else:
        d[word] = 1

print(d)
print("Most frequent word is:", most_fre_word)