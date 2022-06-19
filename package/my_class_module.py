
class Stack:
    "A well-known data structure…"
    def __init__(self):        # constructor
        self.items = []

    def push(self, x):
        self.items.append(x)    # the sky is the limit

    def pop(self):
        x = self.items[-1]        # what happens if it’s empty?
        del self.items[-1]
        return x

    def empty(self):
        return len(self.items) == 0    # Boolean result
