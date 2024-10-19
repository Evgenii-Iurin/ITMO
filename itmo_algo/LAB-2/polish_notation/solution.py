"""
H. Постфиксная запись
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.

Дано выражение в обратной польской записи. Определите его значение.

Входные данные
В единственной строке записано выражение в постфиксной записи, содержащее однозначные числа и операции +, -, *. Строка содержит не более 100 чисел и операций.

Выходные данные
Необходимо вывести значение записанного выражения. Гарантируется, что результат выражения, а также результаты всех промежуточных вычислений по модулю меньше 231.
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

def main():
    input_seq = list(map(str, input().split()))
    stack = Stack()

    for element in input_seq:
        if element == "+":
            x = stack.pop()
            y = stack.pop()
            stack.push(x + y)

        elif element == "-":
            x = stack.pop()
            y = stack.pop()
            stack.push(y - x)

        elif element == "*":
            x = stack.pop()
            y = stack.pop()
            stack.push(x * y)
        else:
            stack.push(int(element))
    
    return stack.get_last()


if __name__ == "__main__":
    print(main())