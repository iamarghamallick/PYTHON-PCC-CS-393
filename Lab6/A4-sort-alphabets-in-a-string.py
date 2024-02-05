# 4. Write a program to sort the alphabets in a string(without using sort function)

def sort(str):
    chars = list(str)
    n = len(chars)
    for i in range(n-1):
        for j in range(n-1-i):
            if chars[j] > chars[j+1]:
                # swap
                chars[j], chars[j+1] = chars[j+1], chars[j]
    sorted_str = ''.join(chars)
    return sorted_str

print(sort("ARGHAMALLICK"))