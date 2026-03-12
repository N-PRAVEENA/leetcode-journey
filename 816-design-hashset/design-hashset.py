class MyHashSet(object):

    def __init__(self):
        self.arr = set()

    def add(self, key):
        self.arr.add(key)

    def remove(self, key):
        if key in self.arr:
            self.arr.remove(key)

    def contains(self, key):
        if key in self.arr:
            return True
        else:
            return False