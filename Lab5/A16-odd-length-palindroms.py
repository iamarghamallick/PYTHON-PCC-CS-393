# A16. Write a program to find all odd length palindromes from a list.

def is_palindrome(s):
    return s == s[::-1]

def odd_length_palindromes(strings):
    odd_palindromes = []
    for string in strings:
        if len(string)%2 != 0:
            odd_palindromes.append(string)
    return odd_palindromes

string_list = ["argha", "level", "deified", "python", "radar", "good", "madam", "hello"]

odd_palindromes = odd_length_palindromes(string_list)
print("Odd length palindromes:", odd_palindromes)
