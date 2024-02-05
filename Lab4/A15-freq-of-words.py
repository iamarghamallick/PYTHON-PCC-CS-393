# A15. The program takes a string and counts the frequency of words appearing in that string using a dictionary.

sentence = "this is a sample input string it contains multiple words some of which are repeated words like this is a sample and words appear more than once in this string"
dic = {}
sentence_list = sentence.split(sep=" ")
for word in sentence_list:
    if dic.__contains__(word):
        dic[word] = int(dic.get(word)) + 1
    else:
        dic[word] = 1
print(dic)