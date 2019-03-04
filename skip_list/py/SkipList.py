import random
class SkipNode:
    def __init__(self, height, key):
        self.key = key
        self.next = [None] * height

class SkipList:
    def __init__(self):
        self.head = SkipNode(1, float("-inf"))
        self.head.next[0] = SkipNode(0, float("inf"))
        self.length = 0

    def randomHeight(self, probability = 0.5):
        level = 1
        while random.random() < probability:
            level += 1
        return level

    def getPath(self, elem):
        levels = len(self.head.next)
        path = [None] * levels
        curr = self.head
        for i in range(levels - 1, -1, -1):
            while curr.next[i].key < elem:
                curr = curr.next[i]
            path[i] = curr
        return path

    def add(self, elem):
        node = SkipNode(self.randomHeight(), elem)
        while len(self.head.next) < len(node.next):
            self.head.next.append(SkipNode(0, float("inf")))
     
        path = self.getPath(elem)            
        if path[0].next[0].key == elem:
            return
        
        for i in range(len(node.next)):
            node.next[i] = path[i].next[i]
            path[i].next[i] = node
        self.length += 1

    def floor(self, elem):
        path = self.getPath(elem)            
        if path[0].next[0].key == elem:
            return path[0].next[0].key
        return path[0].key

    def ceiling(self, elem):
        path = self.getPath(elem)            
        return path[0].next[0].key

    def find(self, elem):
        path = self.getPath(elem)            
        if path[0].next[0].key == elem:
            return path[0].next[0]
        return None

    def __contains__(self, elem):
        return self.find(elem) is not None

    def remove(self, elem):
        path = self.getPath(elem)
        curr = path[0].next[0]
        if curr.key != elem:
            raise KeyError(elem)
        for i in range(len(curr.next)):
            path[i].next[i] = path[i].next[i].next[i]
        self.length -= 1

    def __len__(self):
        return self.length
