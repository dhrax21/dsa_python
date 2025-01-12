from collections import deque

# q=deque()
#
# for n in range(1,10):
#     q.append(n)
#
# print(q)
# q.reverse()
# print(q)
# print(q.popleft())

class Queue:

    def __init__(self):
        self.buffer=deque()

    def enqueue(self,val):
        self.buffer.append(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)