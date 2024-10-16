"""
РЕКУРЕТНЫЙ СПОСОБО НЕ ПРОШЕЛ ПО ВРЕМЕНИ (МЕДЛЕННЫЙ)

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


def count_similar(balls, l_pointer, r_pointer):

    if (len(balls) <= 2):
        return 0
  
    while balls and (
        r_pointer != len(balls) - 1 and
        l_pointer != len(balls) - 2
    ):
        while r_pointer <= len(balls) - 1 and balls[l_pointer] == balls[r_pointer]:
            r_pointer += 1

        if r_pointer - l_pointer > 2:
            balls = remove_similar_from_seq(balls, l_pointer, r_pointer)
            return (r_pointer - l_pointer) + count_similar(balls, l_pointer=0, r_pointer=1)
        else:
            l_pointer = r_pointer
            r_pointer += 1
    return 0

def remove_similar_from_seq(balls, l_pointer, r_pointer):
    return balls[:l_pointer] + balls[r_pointer:]
    

def main():
    input_seq = list(map(int, input().split()))
    return count_similar(input_seq[1:], 0, 1)
    


if  __name__ == "__main__":
    print(main())