def no_dups(s):
    # Your code here
    string = s.split()
    print(string)
    # unique = set(string)
    words = set()

    # no_dups = set(string)
    # new_string = ' '.join(no_dups)
    # print(new_string)
    # return  new_string # print(string)


    return_string = ""
    # list = 
    for word in string:
        if word not in words:
            return_string += f" {word}"
            words.add(word)


            # return_string = return_string.join(word)
    # list_string = [s for s in words]
    # return_string = "".join(list_string)

    print(return_string.strip())
    return return_string.strip()

    # new_string = "".join(w for w in unique)
    # print(new_string)
    # return new_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))