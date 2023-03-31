def quick_sort(alist, pivot):
    if len(alist) == 0:
        return None
    compareCount = 0
    smaller, same, larger = [], [], []
    for i in range(len(alist)):
        if alist[i] < pivot:
            smaller.append(alist[i])
            compareCount += 1
        elif alist[i] > pivot:
            larger.append(alist[i])
            compareCount += 2
        else:
            same.append(alist[i])
            compareCount += 2
    smaller.sort()
    larger.sort()
    alist.clear()
    alist.append(smaller)
    alist.append(same)
    alist.append(larger)
    return compareCount


def median(a, b, c):
    if a > b ^ a > c:
        return a
    elif b > a ^ b > c:
        return b
    else:
        return c
