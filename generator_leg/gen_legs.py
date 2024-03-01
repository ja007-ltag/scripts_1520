"""
Файл для генерации ног логических объектов.

данные помещать в legs_in.
Пример его заполнения:
-1 SI1C
01 AB_1C
10 AB_1N
1- SI1N
"""

def line_leg(leg, neighbour, neighbours_leg):
    neighbour = f'{neighbour:>12}'
    return f'  {leg:>4} {neighbour:31} {neighbours_leg}'

def test_line_leg():
    assert line_leg('0', 'LB1N', '1') == '     0         LB1N                    1'
    assert line_leg('1', 'LN_N3P_C', '0') == '     1     LN_N3P_C                    0'
    assert line_leg('1', 'LN_N3P_CLN_N3P_C', '0') == '     1 LN_N3P_CLN_N3P_C                0'

if __name__ == '__main__':
    # Читаем файл и удаляем пустые строки
    objects = [line.split() for line in open('legs_in') if line.strip()]
    # [('-', 'SI1C', '1'), ('0', 'AB_1C', '1'), ('1', 'AB_1N', '0'), ('1', 'SI1N', '-')]
    objects = [(line[0][0], line[1], line[0][1]) for line in objects]

    print(objects)
    # [('-', 'SI1C', '1'), ('0', 'AB_1C', '1'), ('1', 'AB_1N', '0'), ('1', 'SI1N', '-')]

    add_left = lambda: f'{line_leg(L, objects[i - 1][1], objects[i - 1][2])}\n'
    add_right = lambda: f'{line_leg(R, objects[i + 1][1], objects[i + 1][0])}\n'

    with open('legs_out', 'w', newline='\n') as f:
        for i in range(len(objects)):
            L, name, R = objects[i]  # ('0', 'AB_1C', '1')

            res = f'{name}\n'

            if L == '-': # левого объекта нет
                res += add_right()
            elif R == '-': # правого объекта нет
                res += add_left()
            elif L < R: # левая нога младше
                res += add_left()
                res += add_right()
            elif R < L:
                res += add_right()
                res += add_left()
            else:
                raise ValueError(f'ERROR! Проверь ноги у объекта: {name}')

            f.write(res + '\n')
            # print(res)
