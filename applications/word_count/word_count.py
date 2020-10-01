def word_count(s):
    # Your code here
    my_string = s.lower().split()
    print(my_string)
    dict = {}
    ignore = {',','"',':',';','.', '-', '+', '=', '/', '\\' , '|', '[', ']' , '{', '}','(', ')', '*', '^', '&'}
    for word in my_string:
        # word = raw_word.strip(ignore)
        # word = "".join(c for c in word if c.isalpha())
        new_word = "".join(c for c in word if c not in ignore)
        if len(new_word) == 0:
            return dict
        print(new_word)
        if new_word not in dict:
            dict[new_word] = 0

        dict[new_word] += 1
    print(dict)
    return dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))