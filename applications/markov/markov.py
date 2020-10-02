import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    data = words.split()

# TODO: analyze which words can follow other words
# Your code here
    dict = {}
    for i in range(len(data) - 1):
        if data[i] not in dict:
            dict[data[i]] = []
        dict[data[i]].append(data[i+1])
    
    starters = [word for word in data if word[0].isupper() and word[-1].isalpha()]

    def is_stopper(word):
        punct = { "'",'"', '!', '?', '.'}
        if word[-1] in punct:
            return True
        elif len(word) >= 2 and word[-2] in punct:
            if word[-1] == '"':
                return True
        else:
            return False
    stoppers = [word for word in data if is_stopper(word)]


# TODO: construct 5 random sentences
# Your code here
    def sentence_gen(dict, starters, stoppers):
        # stop = set(stoppers)
        start = random.choice(starters)
        print(start, end=" ")
        # while is_stopper(random.choice(dict[start])) ==False:
        #     print(random.choice(dict[start]), end=" ")
        word = random.choice(dict[start])
        while is_stopper(word) == False:
            print(word, end=" ")
            word = random.choice(dict[word])
        print(random.choice(stoppers))
        # print(random.choice(starters))
        # print(random.choice(stoppers))

    for i in range(5):
        sentence_gen(dict, starters, stoppers)
        print("")

