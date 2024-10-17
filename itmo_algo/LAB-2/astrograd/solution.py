# class DequeFromList:
#     def __init__(self):
#         self.elements = [] 
#         self.head = 0
#         self.tail = 0
    
#     def append(self, value):
#         """Append value to the tail (end) of the list."""
#         if self.tail < len(self.elements):
#             self.elements[self.tail] = value
#         else:
#             self.elements.append(value)
#         self.tail += 1
    
#     def remove_front(self):
#         """Remove element from the front by incrementing head pointer."""
#         if self.head == self.tail:
#             raise IndexError("Deque is empty!")
#         value = self.elements[self.head]
#         self.head += 1
#         return value
    
#     def is_empty(self):
#         """Check if the deque is empty."""
#         return self.head == self.tail
    
#     def front(self):
#         """Return the element at the front without removing it."""
#         if self.is_empty():
#             raise IndexError("Deque is empty!")
#         return self.elements[self.head]


def main():
    n_actions = input()
    smap = [None] * (10**5 + 1)
    stack = []
    head = 0

    for _ in range(int(n_actions)):
        action = list(map(int, input().split()))
        
        if action[0] == 1:
            id = action[1]
            if not stack:
                stack.append(id)
                smap[id] = 0
            else:
                smap[id] = smap[stack[-1]] + 1
                stack.append(id)

        if action[0] == 2:
            head += 1

        if action[0] == 3:
            stack.pop()

        if action[0] == 4:
            id = action[1]
            people_in_fron_of = smap[id] - smap[stack[head]]
            print(people_in_fron_of)
        
        if action[0] == 5:
            print(stack[0])


if __name__ == "__main__":
    main()