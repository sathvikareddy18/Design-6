from collections import deque

class PhoneDirectory:

    def __init__(self, maxNumbers):
        self.q = deque()
        self.usedSet = set()

        for i in range(maxNumbers):
            self.q.append(i)

    def get(self):
        if not self.q:
            return -1
        num = self.q.popleft()
        self.usedSet.add(num)
        return num

    def check(self, number):
        return number not in self.usedSet

    def release(self, number):
        if number not in self.usedSet:
            return
        self.usedSet.remove(number)
        self.q.append(number)
