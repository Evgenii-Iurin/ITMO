"""
A. Скобки
ограничение по времени на тест 2 секунды
ограничение по памяти на тест 256 мегабайт
Требуется определить, является ли правильной данная последовательность круглых, квадратных и фигурных скобок.

Входные данные
В единственной строке входного файла записано подряд N скобок (1 ≤ N ≤ 10^5).

Выходные данные
В выходной файл вывести «YES», если данная последовательность является правильной, и «NO» в противном случае.
"""


class Stack():
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

class Mapper():
    def __init__(self):
        self.brackets = ["(", ")", "{", "}", "[", "]"]
    
    def check_open_bracket(self, bracket):
        if bracket in ['(', '{', '[']:
            return True
        else:
            return False
    def get_pair_for_bracket(self, bracket):
        open_bracket_index = self.brackets.index(bracket) - 1
        return self.brackets[open_bracket_index]


def main():
    brackets = input()

    stack = Stack()
    mapper = Mapper()

    for bracket in brackets:
        if mapper.check_open_bracket(bracket):
            stack.push(bracket)
        elif (not stack.is_empty()) and (mapper.get_pair_for_bracket(bracket) == stack.get_last()):
            stack.pop()
        else:
            return 'NO'
    
    if stack.is_empty():
        return 'YES'
    else: 
        return 'NO'

if  __name__ == "__main__":
    print(main())