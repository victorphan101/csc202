import datetime
import random
from unittest import TestCase

import sorts


class Test_Sorts(TestCase):
    #Insertion Sort
    def test_insertion_sort_1k_print(self):
        insertList1K = []
        for i in range(1000):
            num = random.randint(0, 100)
            insertList1K.append(num)
        print("Insertion 1K comparisons: " + str(sorts.insertion_sort(insertList1K)))

    def test_insertion_sort_1k_time(self):
        insertList1K = []
        for i in range(1000):
            num = random.randint(0, 100)
            insertList1K.append(num)
        begin_time = datetime.datetime.now()
        sorts.insertion_sort(insertList1K)
        print(datetime.datetime.now() - begin_time)

    def test_insertion_sort_2k_print(self):
        insertList2K = []
        for i in range(2000):
            num = random.randint(0, 100)
            insertList2K.append(num)
        print("Insertion 2K comparisons: " + str(sorts.insertion_sort(insertList2K)))

    def test_insertion_sort_2k_time(self):
        insertList2K = []
        for i in range(2000):
            num = random.randint(0, 100)
            insertList2K.append(num)
        begin_time = datetime.datetime.now()
        sorts.insertion_sort(insertList2K)
        print(datetime.datetime.now() - begin_time)

    def test_insertion_sort_4k_print(self):
        insertList4K = []
        for i in range(4000):
            num = random.randint(0, 100)
            insertList4K.append(num)
        print("Insertion 4K comparisons: " + str(sorts.insertion_sort(insertList4K)))

    def test_insertion_sort_4k_time(self):
        insertList4K = []
        for i in range(4000):
            num = random.randint(0, 100)
            insertList4K.append(num)
        begin_time = datetime.datetime.now()
        sorts.insertion_sort(insertList4K)
        print(datetime.datetime.now() - begin_time)

    def test_insertion_sort_8k_print(self):
        insertList8K = []
        for i in range(8000):
            num = random.randint(0, 100)
            insertList8K.append(num)
        print("Insertion 8K comparisons: " + str(sorts.insertion_sort(insertList8K)))

    def test_insertion_sort_8k_time(self):
        insertList8K = []
        for i in range(8000):
            num = random.randint(0, 100)
            insertList8K.append(num)
        begin_time = datetime.datetime.now()
        sorts.insertion_sort(insertList8K)
        print(datetime.datetime.now() - begin_time)

    def test_insertion_sort_16k_print(self):
        insertList16K = []
        for i in range(16000):
            num = random.randint(0, 100)
            insertList16K.append(num)
        print("Insertion 16K comparisons: "+ str(sorts.insertion_sort(insertList16K)))

    def test_insertion_sort_16k_time(self):
        insertList16K = []
        for i in range(16000):
            num = random.randint(0, 100)
            insertList16K.append(num)
        begin_time = datetime.datetime.now()
        sorts.insertion_sort(insertList16K)
        print(datetime.datetime.now() - begin_time)

    def test_insertion_sort_32k_print(self):
        insertList32K = []
        for i in range(32000):
            num = random.randint(0, 100)
            insertList32K.append(num)
        print("Insertion 32K comparisons: " + str(sorts.insertion_sort(insertList32K)))

    def test_insertion_sort_32k_time(self):
        insertList32K = []
        for i in range(32000):
            num = random.randint(0, 100)
            insertList32K.append(num)
        begin_time = datetime.datetime.now()
        sorts.insertion_sort(insertList32K)
        print(datetime.datetime.now() - begin_time)


    # Selection Sort
    def test_selection_sort_1k_print(self):
        selectionList1K = []
        for i in range(1000):
            num = random.randint(0, 100)
            selectionList1K.append(num)
        print("Selection 1K comparisons: " + str(sorts.selection_sort(selectionList1K)))

    def test_selection_sort_1k_time(self):
        selectionList1K = []
        for i in range(1000):
            num = random.randint(0, 100)
            selectionList1K.append(num)
        begin_time = datetime.datetime.now()
        sorts.selection_sort(selectionList1K)
        print(datetime.datetime.now() - begin_time)

    def test_selection_sort_2k_print(self):
        selectionList2K = []
        for i in range(2000):
            num = random.randint(0, 100)
            selectionList2K.append(num)
        print("Selection 2K comparisons: " + str(sorts.selection_sort(selectionList2K)))

    def test_selection_sort_2k_time(self):
        selectionList2K = []
        for i in range(2000):
            num = random.randint(0, 100)
            selectionList2K.append(num)
        begin_time = datetime.datetime.now()
        sorts.selection_sort(selectionList2K)
        print(datetime.datetime.now() - begin_time)
    
    def test_selection_sort_4k_print(self):
        selectionList4K = []
        for i in range(4000):
            num = random.randint(0, 100)
            selectionList4K.append(num)
        print("Selection 4K comparisons: " + str(sorts.selection_sort(selectionList4K)))

    def test_selection_sort_4k_time(self):
        selectionList4K = []
        for i in range(4000):
            num = random.randint(0, 100)
            selectionList4K.append(num)
        begin_time = datetime.datetime.now()
        sorts.selection_sort(selectionList4K)
        print(datetime.datetime.now() - begin_time)

    def test_selection_sort_8k_print(self):
        selectionList8K = []
        for i in range(8000):
            num = random.randint(0, 100)
            selectionList8K.append(num)
        print("Selection 8K comparisons: " + str(sorts.selection_sort(selectionList8K)))

    def test_selection_sort_8k_time(self):
        selectionList8K = []
        for i in range(8000):
            num = random.randint(0, 100)
            selectionList8K.append(num)
        begin_time = datetime.datetime.now()
        sorts.selection_sort(selectionList8K)
        print(datetime.datetime.now() - begin_time)

    def test_selection_sort_16k_print(self):
        selectionList16K = []
        for i in range(16000):
            num = random.randint(0, 100)
            selectionList16K.append(num)
        print("Selection 16K comparisons: " + str(sorts.selection_sort(selectionList16K)))

    def test_selection_sort_16k_time(self):
        selectionList16K = []
        for i in range(16000):
            num = random.randint(0, 100)
            selectionList16K.append(num)
        begin_time = datetime.datetime.now()
        sorts.selection_sort(selectionList16K)
        print(datetime.datetime.now() - begin_time)

    def test_selection_sort_32k_print(self):
        selectionList32K = []
        for i in range(32000):
            num = random.randint(0, 100)
            selectionList32K.append(num)
        print("Selection 32K comparisons: " + str(sorts.selection_sort(selectionList32K)))

    def test_selection_sort_32_time(self):
        selectionList32K = []
        for i in range(32000):
            num = random.randint(0, 100)
            selectionList32K.append(num)
        begin_time = datetime.datetime.now()
        sorts.selection_sort(selectionList32K)
        print(datetime.datetime.now() - begin_time)
