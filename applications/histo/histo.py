# Your code here
import string

def word_count(file):
    ignore = {',','"',':',';','.', '-', '+', '=', '/', '\\' , '|', '[', ']' , '{', '}','(', ')', '*', '^', '&'}
    dict = {}
    file = open(file, "r")
    data = file.read()
    words = data.lower().split()
    for word in words:
        # print(word)
        # new_word = word.strip()
        word = word.translate(str.maketrans('', '', string.punctuation))
        if word not in dict:
            dict[word] = "#"
        dict[word] += "#"
    # print(dict)
    # return dict
    items = list(dict.items())
    items.sort(key=lambda t: (-len(t[1]), t[0]))
    # items = sorted(items, key=lambda t: t[1], reverse=True)
    # sorted(items, key=lambda t: t[0])
    

    for i in items:
        print(f"{i[0]:20}  {i[1]}")
    # for item in dict:
    #     print(f"{item}: {dict[item]}")


word_count("robin.txt")
