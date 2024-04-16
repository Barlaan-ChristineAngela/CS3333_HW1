class Queue:

    def __init__(self):
        self.newQueue = []

    def enqueue(self, item):
        self.newQueue.append(item)
        return self.newQueue

    def dequeue(self):
        self.newQueue.pop()
        return self.newQueue

    def peek(self):
        if self.newQueue:
            item = self.newQueue[0]
            return item
        else:
            print("Queue is empty")

    def empty(self):
        return len(self.newQueue) == 0

    def front(self):
        if self.newQueue:
            return self.newQueue[0]
        else:
            print("Queue is empty")

    def rear(self):
        if self.newQueue:
            return self.newQueue[-1]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.newQueue)
