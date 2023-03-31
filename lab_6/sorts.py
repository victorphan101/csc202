def insertion_sort(alist):
    if len(alist) == 0:
        return None
    compareCount = 0
    for i in range(1, len(alist)):
        j = i-1
        while j >= 0 and alist[j] < alist[j-1]:
            compareCount += 1
            alist[j], alist[j-1] = alist[j-1], alist[j]
            j -= 1
    return compareCount


def selection_sort(alist):
    compareCount = 0
    if len(alist) == 0:
        return None
    index = 0
    for i in range(len(alist)):
        currMin = alist[i]
        for j in range(i+1, len(alist)):
            compareCount += 1
            if alist[j] < currMin:
                currMin = alist[j]
                index = j
        alist[index] = alist[i]
        alist[i] = currMin
    return compareCount
