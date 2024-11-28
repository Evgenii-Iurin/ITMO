"""
ограничение по времени на тест 1 секунда
ограничение по памяти на тест 256 мегабайт

В одной компьютерной игре игрок выставляет в линию шарики разных цветов. Когда образуется непрерывная цепочка из трех и более шариков одного цвета, она удаляется из линии. При этом все шарики сдвигаются друг к другу и ситуация может повториться.

Напишите программу, которая по данной ситуации определяет, сколько шариков будет сейчас уничтожено. Естественно, непрерывных цепочек из трех и более одноцветных шаров в начальный момент может быть не более одной.

Входные данные
Даны количество шариков в цепочке (не более 105
) и цвета шариков (от 0 до 9, каждому цвету соответствует свое целое число).

Выходные данные
Требуется вывести количество шариков, которые будут уничтожены.

"""


def remove_n_last_elements(stack, n):
    total_remove = 0
    for _ in range(n):
        stack.pop()
        total_remove += 1
    return stack, total_remove



def count_similar(n, input_seq):
    stack = []
    res = 0
    for i in range(n):
        value = input_seq[i]
        
        if stack:
            if value == stack[-1][0]: # if last value in stack the same as current value
                stack.append([value, stack[-1][1] + 1]) # increase counter
            else:
                if stack[-1][1] > 2: # else check the last counter value in stack
                    stack, total_removed = remove_n_last_elements(stack, stack[-1][1]) # remove elements from stack if we have 'set'
                    res += total_removed     
                    if value == stack[-1][0]: # after the removing we should compare current value and last one
                        stack.append([value, stack[-1][1] + 1]) # if they are the same, increase the counter
                    else:
                        stack.append([value, 1]) # else just add with counter = 1 because it's a new element in sequence
                else:
                    stack.append([value, 1]) # if the last sequence is not enough to be deleted, add new element with count = 1
        else: # if stack is empty
            stack.append([value, 1])
    
    if stack[-1][1] > 2:
        res += stack[-1][1]

    return res

def main():
    input_seq = list(map(int, input().split()))
    return count_similar(input_seq[0], input_seq[1:])

if __name__ == "__main__":
    print(main())
