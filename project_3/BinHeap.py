class MyException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class BinHeap:
    def __init__(self, capacity):
        self.arrayList = [None] * capacity
        self.numElem = 0
        self.capacity = capacity

    def size(self):
        return self.numElem

    def is_Empty(self):
        return self.numElem == 0

    def is_full(self):
        return self.numElem == self.capacity

    def resizeArray(self):
        self.capacity *= 2
        newArray = [None] * self.capacity
        pointer = 0
        for i in self.arrayList:
            newArray[pointer] = i
            pointer += 1
        self.arrayList = newArray
        return self.capacity

    def insert(self, item):
        if self.is_full():
            self.resizeArray()
        if self.is_Empty():
            self.arrayList[0] = item
            self.numElem += 1
            return
        self.arrayList[self.numElem] = item
        return self.swapUp(item, self.numElem)

    def swapUp(self, item, index):
        if index > 0:
            if (index - 1) % 2 == 0:
                parentLeft = int((index - 1) / 2)
                if item <= self.arrayList[parentLeft]:
                    tmp = self.arrayList[index]
                    self.arrayList[index] = self.arrayList[parentLeft]
                    self.arrayList[parentLeft] = tmp
                    return self.swapUp(item, parentLeft)
            elif (index - 2) % 2 == 0:
                parentRight = int((index - 2) / 2)
                if item <= self.arrayList[parentRight]:
                    tmp = self.arrayList[index]
                    self.arrayList[index] = self.arrayList[parentRight]
                    self.arrayList[parentRight] = tmp
                    return self.swapUp(item, parentRight)
        self.numElem += 1
        print(self.numElem)
        return item

    def deleteMin(self):
        if self.numElem == 0:
            raise MyException("The Heap is Empty")
        print(self.numElem)
        tmp = self.arrayList[self.numElem-1]
        self.arrayList[0] = tmp
        self.arrayList[self.numElem - 1] = None
        self.numElem -= 1
        print(self.arrayList[0])
        print(self.numElem)
        return self.swapDown(0)

    def swapDown(self, index):
        if self.arrayList[(index * 2) + 1] is not None and self.arrayList[index] > self.arrayList[(index * 2) + 1]:
            print("swap time")
            tmp = self.arrayList[index]
            self.arrayList[index] = self.arrayList[(index * 2) + 1]
            self.arrayList[(index * 2) + 1] = tmp
            print(self.arrayList)
            return self.swapDown((index * 2) + 1)
        elif self.arrayList[index * 2 + 2] is not None and self.arrayList[index] > self.arrayList[index * 2 + 2]:
            print("swap time")
            tmp = self.arrayList[index]
            self.arrayList[index] = self.arrayList[index * 2 + 2]
            self.arrayList[index * 2 + 2] = tmp
            return self.swapDown((index * 2) + 2)
        print(self.arrayList[0])
        if (index-1) % 2 == 0:
            return self.arrayList[int((index-1)/2)]
        return self.arrayList[int((index-2)/2)]

    def _string_(self):
        result = ""
        for i in self.arrayList:
            result = result + str(i) + " "
        return result
