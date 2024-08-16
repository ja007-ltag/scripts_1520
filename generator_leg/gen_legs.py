"""
Файл для генерации ног логических объектов.

Данные помещать в legs_in.
Пример его заполнения как в yard.draw через [TAB]:
<- SI1C 1>	<0 AB_1C 1>	<1 AB_1N 0>	<1 SI1N ->

Легче всего распознать граф в visio файле, сгенерить yard.draw и взять оттуда необходимые строки
"""

def line_leg(leg, neighbour, neighbours_leg):
    neighbour = f'{neighbour:>12}'
    return f'  {leg:>4} {neighbour:31} {neighbours_leg}'

def test_line_leg():
    assert line_leg('0', 'LB1N', '1') == '     0         LB1N                    1'
    assert line_leg('1', 'LN_N3P_C', '0') == '     1     LN_N3P_C                    0'
    assert line_leg('1', 'LN_N3P_CLN_N3P_C', '0') == '     1 LN_N3P_CLN_N3P_C                0'

if __name__ == '__main__':
    # Читаем из файла строку, и получаем список строк с объектами
    objects = open('legs_in').read().strip().split('\t')
    print(objects)

    # Список кортежей с объектами ног
    # [('-', 'SI1C', '1'), ('0', 'AB_1C', '1'), ('1', 'AB_1N', '0'), ('1', 'SI1N', '-')]
    objects = [(line[1], line.split()[1], line[-2]) for line in objects]
    print(objects)
    print(f'Всего объектов: {len(objects)}')

    add_left = lambda: f'{line_leg(L, objects[i - 1][1], objects[i - 1][2])}\n'
    add_right = lambda: f'{line_leg(R, objects[i + 1][1], objects[i + 1][0])}\n'

    with open('legs_out', 'w', newline='\n') as f:
        for i in range(len(objects)):
            L, name, R = objects[i]  # ('0', 'AB_1C', '1')

            res = f': {name} \n'

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
