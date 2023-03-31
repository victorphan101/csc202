def is_prime(size):
    for i in range(2, int(size ** 0.5) + 1):
        if size % i == 0:
            return False
    return True


def next_prime(x):
    return min([i for i in range(x + 1, 2 * x) if is_prime(i)])


class MyHashTable:
    """sets with key and data"""

    def __init__(self, table_size=11):
        self.table = [[] for _ in range(11)]
        self.num_items = 0
        self.num_collisions = 0
        self.table_size = table_size
        """ load cannot exceed 1.5, need to double size plus 1 if reached"""

    def load_factor(self):
        return self.num_items / self.table_size

    def rehash(self):
        newSize = self.table_size * 2 + 1

        if not is_prime(newSize):
            newSize = next_prime(newSize)

        old_table = self.table
        new_table = [[] * newSize]
        self.table = new_table

        for elem in old_table:
            self.insert(elem[0], elem[1])

    def insert(self, key, item):
        index = key % self.table_size
        if self.load_factor() > 1.5:
            self.rehash()

        if len(self.table[index]) == 0:
            self.table[index].append((key, item))
            self.num_items += 1
            return self.num_items
        else:
            self.table[index].append((key, item))
            self.num_collisions += 1
            self.num_items += 1
            return self.num_collisions

    def get(self, key):
        index = key % self.table_size
        for elem in self.table[index]:
            if elem[0] == key:
                return elem[1]
        return LookupError

    def remove(self, key):
        if self.get(key) is LookupError:
            return LookupError
        index = key % self.table_size
        pointer = 0
        for elem in self.table[index]:
            if elem[0] == key:
                self.table[index].pop(pointer)
                return pointer
            pointer += 1

    def size(self):
        return self.num_items

    def collisions(self):
        return self.num_collisions
