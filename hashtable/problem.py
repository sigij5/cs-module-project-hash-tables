

arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


sum = 0

for i in range(len(arr)):
    smallest = 10000
    for j in range(len(arr[i])):
        if arr[j] < smallest:
            smallest = arr[j]
        sum += smallest
print(sum)
