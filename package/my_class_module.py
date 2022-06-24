
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

class Sorts:
    def __init__(self, unsorted):
        self.items = unsorted

    def initialize_sorted( self, n, x ):
        self.items[n] = x

    def selection_sort(self):

        for idx1 in range( len(self.items) ):

            for idx2 in range( idx1, len(self.items) ):
                  
