def main():
    n_actions = int(input())
    smap = [None] * (10**5 + 1)
    stack = []  
    head = 0  

    for _ in range(n_actions):
        action = list(map(int, input().split()))

        if action[0] == 1:
            id = action[1]
            stack.append(id)
            if len(stack) == 1:
                smap[id] = 0
            else:
                smap[id] = smap[stack[-2]] + 1

        elif action[0] == 2:
            head += 1

        elif action[0] == 3:
            stack.pop()

        elif action[0] == 4:
            id = action[1]
            people_in_front = smap[id] - smap[stack[head]]
            print(people_in_front)

        elif action[0] == 5:
            print(stack[head])


if __name__ == "__main__":
    main()