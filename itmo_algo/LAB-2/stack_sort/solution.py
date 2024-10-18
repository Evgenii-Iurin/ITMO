from collections import deque

def pop_from_stack_B(stack: list, look_for: int, result: list):
    stack.pop()
    look_for += 1
    result.append('pop')
    return stack, look_for, result

def main():
    N = int(input())  
    stack_A = deque(map(int, input().split()))
    stack_B = []
    look_for = 1
    result = []

    while stack_A or stack_B:
        if stack_B and stack_B[-1] == look_for:
            stack_B, look_for, result = pop_from_stack_B(stack_B, look_for, result)

        elif stack_A:
            new_el = stack_A.popleft()
            stack_B.append(new_el)
            result.append('push')
        else:
            return ['impossible']
    return result

if __name__ == "__main__":
    res = main()
    for i in res:
        print(i)
