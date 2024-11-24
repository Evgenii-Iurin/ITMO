import sys

class Stack:
    def __init__(self):
        self.values = []

    def push(self, x):
        self.values.append(x)
    
    def pop(self):
        if not self.is_empty():
            return self.values.pop()
        return None

    def is_empty(self):
        return self.values == []

    def get_last(self):
        if not self.is_empty():
            return self.values[-1]
        return None 

def main():
    number_of_operation = int(input())
    stack = Stack()

    for _ in range(number_of_operation):
        operation = sys.stdin.readline().strip().split()

        if operation[0] == "1":
            x = int(operation[1])
            if stack.is_empty():
                stack.push([x, x])
            else:
                min_value = min(x, stack.get_last()[1])
                stack.push([x, min_value])
        
        elif operation[0] == "2":
            stack.pop()
        
        elif operation[0] == "3":
            print(stack.get_last()[1])

if __name__ == "__main__":
    main()
