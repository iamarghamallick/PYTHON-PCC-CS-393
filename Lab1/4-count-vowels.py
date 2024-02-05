def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)


s = input("Enter a sentence: ")
w = s.split()
sorted_w = sorted(w)
dict = {}
for word in sorted_w:
    num_vowels = count_vowels(word)
    dict[word] = num_vowels
print(dict)
