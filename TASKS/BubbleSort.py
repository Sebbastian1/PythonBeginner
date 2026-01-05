def bubbleSort(sorted):
    x = len(sorted)
    for i in range(x):
        for j in range(x - i - 1):
            if sorted[j] > sorted[j+1]:
                sorted[j], sorted[j+1] = sorted[j+1], sorted[j]
    return sorted





print(bubbleSort([15, 8, 21, 4, 17, -5]))