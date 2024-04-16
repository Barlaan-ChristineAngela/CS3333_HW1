class List:

    def __init__(self):
        self.newList = []

    def append(self, item):
        self.newList.append(item)
        return self.newList

    def copy(self):
        return self.newList.copy()

    def clear(self):
        self.newList.clear()
        return self.newList

    def count(self, item):
        return self.newList.count(item)

    def extend(self, iterable):
        self.newList.extend(iterable)
        return self.newList

    def index(self, item):
        return self.newList.index(item)

    def insert(self, index, item):
        self.newList.insert(index, item)
        return self.newList

    def pop(self, index):
        self.newList.pop(index)
        return self.newList


    def remove(self, item):
        self.newList.remove(item)
        return self.newList

    def reverse(self):
        self.newList.reverse()
        return self.newList

    def sort(self):
        self.newList.sort()
        return self.newList

    def get_min(self):
        return min(self.newList)

    def get_max(self):
        return max(self.newList)