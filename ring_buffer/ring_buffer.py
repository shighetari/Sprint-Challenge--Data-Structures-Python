class RingBuffer:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.free_index = 0

    def append(self, item):
        if len(self.stack) < self.capacity:
            #insert item @ free index
            self.stack.append(item)
        elif len(self.stack) == self.capacity:
            if self.free_index == self.capacity:
                self.free_index = 0
            self.stack.pop(self.free_index)
            self.stack.insert(self.free_index, item)
            self.free_index = self.free_index + 1
    def get(self):
        return self.stack
# testing visually for my sake
# buffer = RingBuffer(3)
# print(buffer.append(1))
# print(buffer.append(2))
# print(buffer.append(3))
# print(buffer.append(4))
# print(buffer.append(5))
# print(buffer.append(6))