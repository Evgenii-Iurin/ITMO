from collections import deque

def move_from_dead_end_to_output(stack: list, look_for: int, result: list):
    stack.pop()
    look_for += 1
    result.append('2 1')
    return stack, look_for, result

def main():
    N = int(input())  
    input_seq = deque(map(int, input().split()))

    stack = []
    result = []
    look_for = 1

    while input_seq or stack:
        if stack and stack[-1] == look_for:
            stack, look_for, result = move_from_dead_end_to_output(stack, look_for, result)

        elif input_seq:
            cariage = input_seq.popleft()
            stack.append(cariage)
            result.append('1 1')
        else:
            return '0'

    return result

if __name__ == "__main__":
    result = main()
    for x in result:
        print(x)
