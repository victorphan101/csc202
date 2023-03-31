import random
from unittest import TestCase

import quicksorts


class Test(TestCase):
    # Ordered at 1st elem
    def test_quick_sort_ordered_first_100(self):
        quickListOrder100 = []
        for i in range(100):
            quickListOrder100.append(i)
        print("Quick Sort 100 Ordered First Index comparisons: " + str(quicksorts.quick_sort(quickListOrder100, quickListOrder100[0])))

    def test_quick_sort_ordered_first_200(self):
        quickListOrder200 = []
        for i in range(200):
            quickListOrder200.append(i)
        print("Quick Sort 200 Ordered First Index comparisons: " + str(quicksorts.quick_sort(quickListOrder200, quickListOrder200[0])))

    def test_quick_sort_ordered_first_400(self):
        quickListOrder400 = []
        for i in range(400):
            quickListOrder400.append(i)
        print("Quick Sort 400 Ordered First Index comparisons: " + str(quicksorts.quick_sort(quickListOrder400, quickListOrder400[0])))

    def test_quick_sort_ordered_first_800(self):
        quickListOrder800 = []
        for i in range(800):
            quickListOrder800.append(i)
        print("Quick Sort 800 Ordered First Index comparisons: " + str(quicksorts.quick_sort(quickListOrder800, quickListOrder800[0])))

    # Ordered at Median
    def test_quick_sort_ordered_median_100(self):
        quickListOrder100 = []
        for i in range(100):
            quickListOrder100.append(i)
        firstElem = quickListOrder100[0]
        middleElem = quickListOrder100[int((len(quickListOrder100) - 1) / 2)]
        lastElem = quickListOrder100[len(quickListOrder100) - 1]
        print("Quick Sort 100 Ordered Median comparisons: " + str(quicksorts.quick_sort(quickListOrder100, quicksorts.median(firstElem, middleElem, lastElem))))

    def test_quick_sort_ordered_median_200(self):
        quickListOrder200 = []
        for i in range(200):
            quickListOrder200.append(i)
        firstElem = quickListOrder200[0]
        middleElem = quickListOrder200[int((len(quickListOrder200) - 1) / 2)]
        lastElem = quickListOrder200[len(quickListOrder200) - 1]
        print("Quick Sort 200 Ordered Median comparisons: " + str(quicksorts.quick_sort(quickListOrder200, quicksorts.median(firstElem, middleElem, lastElem))))

    def test_quick_sort_ordered_median_400(self):
        quickListOrder400 = []
        for i in range(400):
            quickListOrder400.append(i)
        firstElem = quickListOrder400[0]
        middleElem = quickListOrder400[int((len(quickListOrder400) - 1) / 2)]
        lastElem = quickListOrder400[len(quickListOrder400) - 1]
        print("Quick Sort 400 Ordered Median comparisons: " + str(quicksorts.quick_sort(quickListOrder400, quicksorts.median(firstElem, middleElem, lastElem))))

    def test_quick_sort_ordered_median_800(self):
        quickListOrder800 = []
        for i in range(800):
            quickListOrder800.append(i)
        firstElem = quickListOrder800[0]
        middleElem = quickListOrder800[int((len(quickListOrder800) - 1) / 2)]
        lastElem = quickListOrder800[len(quickListOrder800) - 1]
        print("Quick Sort 800 Ordered Median comparisons: " + str(quicksorts.quick_sort(quickListOrder800, quicksorts.median(firstElem, middleElem, lastElem))))

    # Random at First Elem
    def test_quick_sort_random_first_100(self):
        quickListRandom100 = []
        for i in range(100):
            num = random.randint(0, 100)
            quickListRandom100.append(num)
        print("Quick Sort 100 Random First Index comparisons: " + str(quicksorts.quick_sort(quickListRandom100, quickListRandom100[0])))

    def test_quick_sort_random_first_200(self):
        quickListRandom200 = []
        for i in range(200):
            num = random.randint(0, 100)
            quickListRandom200.append(num)
        print("Quick Sort 200 Random First Index comparisons: " + str(quicksorts.quick_sort(quickListRandom200, quickListRandom200[0])))

    def test_quick_sort_random_first_400(self):
        quickListRandom400 = []
        for i in range(400):
            num = random.randint(0, 100)
            quickListRandom400.append(num)
        print("Quick Sort 400 Random First Index comparisons: " + str(quicksorts.quick_sort(quickListRandom400, quickListRandom400[0])))

    def test_quick_sort_random_first_800(self):
        quickListRandom800 = []
        for i in range(800):
            num = random.randint(0, 100)
            quickListRandom800.append(num)
        print("Quick Sort 800 Random First Index comparisons: " + str(quicksorts.quick_sort(quickListRandom800, quickListRandom800[0])))

    # Random at Median
    def test_quick_sort_random_median_100(self):
        quickListRandom100 = []
        for i in range(100):
            num = random.randint(0, 100)
            quickListRandom100.append(num)
        firstElem = quickListRandom100[0]
        middleElem = quickListRandom100[int((len(quickListRandom100)-1)/2)]
        lastElem = quickListRandom100[len(quickListRandom100)-1]
        print("Quick Sort 100 Random Median comparisons: " + str(quicksorts.quick_sort(quickListRandom100, quicksorts.median(firstElem, middleElem, lastElem))))

    def test_quick_sort_random_median_200(self):
        quickListRandom200 = []
        for i in range(200):
            num = random.randint(0, 100)
            quickListRandom200.append(num)
        firstElem = quickListRandom200[0]
        middleElem = quickListRandom200[int((len(quickListRandom200)-1)/2)]
        lastElem = quickListRandom200[len(quickListRandom200)-1]
        print("Quick Sort 200 Random Median comparisons: " + str(quicksorts.quick_sort(quickListRandom200, quicksorts.median(firstElem, middleElem, lastElem))))

    def test_quick_sort_random_median_400(self):
        quickListRandom400 = []
        for i in range(400):
            num = random.randint(0, 100)
            quickListRandom400.append(num)
        firstElem = quickListRandom400[0]
        middleElem = quickListRandom400[int((len(quickListRandom400)-1)/2)]
        lastElem = quickListRandom400[len(quickListRandom400)-1]
        print("Quick Sort 400 Random Median comparisons: " + str(quicksorts.quick_sort(quickListRandom400, quicksorts.median(firstElem, middleElem, lastElem))))

    def test_quick_sort_random_median_800(self):
        quickListRandom800 = []
        for i in range(800):
            num = random.randint(0, 100)
            quickListRandom800.append(num)
        firstElem = quickListRandom800[0]
        middleElem = quickListRandom800[int((len(quickListRandom800)-1)/2)]
        lastElem = quickListRandom800[len(quickListRandom800)-1]
        print("Quick Sort 800 Random Median comparisons: " + str(quicksorts.quick_sort(quickListRandom800, quicksorts.median(firstElem, middleElem, lastElem))))


