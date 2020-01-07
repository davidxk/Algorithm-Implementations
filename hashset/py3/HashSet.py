
class HashSet(object):
    def __init__(self):
        self.primes = [53, 97, 193, 389, 769, 1543, 3079, 6151, 12289,
                24593, 49157, 98317, 196613, 393241, 786433, 1572869,
                3145739, 6291469, 12582917, 25165843, 50331653,
                100663319, 201326611, 402653189, 805306457, 1610612741]
        self.primeIdx = 0
        self.table = [[] for _ in range(self.primes[self.primeIdx])]
        self.size = 0
    
    def __len__(self):
        return self.size

    def add(self, value):
        cell = self.table[hash(value) % len(self.table)]
        try:
            cell.index(value)
        except ValueError:
            self.size += 1
            cell.append(value)
            if self.size > self.primes[self.primeIdx]:
                self.rehash()

    def remove(self, value):
        cell = self.table[hash(value) % len(self.table)]
        try:
            cell.remove(value)
            self.size -= 1
        except ValueError:
            raise KeyError(value)

    def __contains__(self, value):
        cell = self.table[hash(value) % len(self.table)]
        try:
            cell.index(value)
            return True
        except ValueError:
            return False

    def discard(self, value):
        cell = self.table[hash(value) % len(self.table)]
        try:
            cell.remove(value)
            self.size -= 1
        except ValueError:
            pass

    def clear(self):
        self.table = [[]] * self.primes[self.primeIdx]
        self.size = 0

    def rehash(self):
        oldTable = self.table
        self.primeIdx += 1
        self.table = [[] for _ in range(self.primes[self.primeIdx])]
        self.size = 0
        for cell in oldTable:
            for value in cell:
                self.add(value)
