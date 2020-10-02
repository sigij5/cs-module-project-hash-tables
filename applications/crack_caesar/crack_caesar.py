# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open("ciphertext.txt") as f:
    encoded = f.read()
# Your code here
freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G',
        'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
# print(len(freq))

dic = {}
for i in encoded:
    if i in freq:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

dic = {k: v for k, v in sorted(
    dic.items(), key=lambda item: item[1], reverse=True)}
print(dic)
# print(dic)
index = 0
for key in dic:
    dic[key] = freq[index]
    index += 1
# print(index)
print(dic)
# print(dic)
decoded = str(encoded)
for i in range(0, len(encoded)):
    if encoded[i] in freq:
        decoded = decoded.replace(decoded[i], dic[encoded[i]])

# for i in range(0, len(encoded)):
#     if encoded[i] in freq:
#         decoded.replace(decoded[i], dic[encoded[i]])
    # print(decoded[i])
print(decoded)