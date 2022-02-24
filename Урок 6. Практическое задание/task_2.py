"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile

@profile
def test_func(num):
    def func(num, start=-2):
            if num == 0:
                # print(f'return base {start}')
                return 0
            else:
                start = start / (-2)
                # print(f'return num {num} start  {start}')
                return func(num - 1, start) + start
    return func(num)

res = test_func(3)
print(f'результат обработки данных {res}')
'''т.к. профилировщик memory_profiler перехватывает только
одну внешнюю функцию, а при рекурсии функция постоянно 
вызывает сама себя то если рекурсивную функцию обернуть
внешней то профилировщик сработает только на нее'''

