line_txt = '''0, LB1N, 1
0, LN_N1P_C, 1
0, LN_N3P_C, 1
0, LN_N5P_C, 1
0, LN_N7P_C, 1
0, LN_N9P_C, 1
0, LN_N11P_C, 1
0, LN_N13P_C, 1
0, LN_N15P_C, 1
0, LN_N17P_C, 1
0, LN_N19P_C, 1
0, LN_N21P_C, 1
0, LN_N23P_C, 1
0, LN_N25P_C, 1
0, LN_N27P_C, 1
0, LN_N29P_C, 1
0, LN_N31P_C, 1
0, LN_N33P_C, 1
0, LN_N35P_C, 1
0, LN_N37P_C, 1
1, LN_N1P_N, 0
1, LN_N3P_N, 0
1, LN_N5P_N, 0
1, LN_N7P_N, 0
1, LN_N9P_N, 0
1, LN_N11P_N, 0
1, LN_N13P_N, 0
1, LN_N15P_N, 0
1, LN_N17P_N, 0
1, LN_N19P_N, 0
1, LN_N21P_N, 0
1, LN_N23P_N, 0
1, LN_N25P_N, 0
1, LN_N27P_N, 0
1, LN_N29P_N, 0
1, LN_N31P_N, 0
1, LN_N33P_N, 0
1, LN_N35P_N, 0
1, LN_N37P_N, 0
0, HB1N_REU_JEL, -'''

all_objects = line_txt.split('\n')
all_objects = [cur.split(', ') for cur in all_objects]

total_all = []
for i in range(len(all_objects)):
    total = ''
    if i != 0 and i != (len(all_objects) - 1):

        cur = all_objects[i]  # ['0', 'LN_N1P_C', '1']
        cur_name = cur[1]  # ['LN_N1P_C']

        print(f'Обрабатываю объект {cur_name}')

        # определяем соседей, их номера и ногу соседа
        if cur[0] == '0':  # если нулевая нога слева
            # "neighbour" = "сосед"
            neighbour_leg0_name = all_objects[i - 1][1]
            neighbour_leg0_leg_num = all_objects[i - 1][2]
            neighbour_leg1_name = all_objects[i + 1][1]
            neighbour_leg1_leg_num = all_objects[i + 1][0]
        else:  # иначе нулевая нога справа
            neighbour_leg0_name = all_objects[i + 1][1]
            neighbour_leg0_leg_num = all_objects[i + 1][0]
            neighbour_leg1_name = all_objects[i - 1][1]
            neighbour_leg1_leg_num = all_objects[i - 1][2]

        total = f'  External name: {cur_name:19} Type: LINE_ALSO      \n' \
                f'. ========================================================\n' \
                f'\n' \
                f'  Leg:   Neighbour:      Neighbours leg:\n' \
                f'. --------------------------------------\n'

        total += f'     {f"0 {neighbour_leg0_name:>12}":33} {neighbour_leg0_leg_num}\n' \
                 f'     {f"1 {neighbour_leg1_name:>12}":33} {neighbour_leg1_leg_num}\n'

        total += f'\n' \
                 f'  Individualizations\n' \
                 f'. ------------------\n' \
                 f'\n' \
                 f'  Order variable   Logical object  Status variable\n' \
                 f'. --------------------------------------------------------\n' \
                 f'\n' \
                 f'  Order variable         IPU object\n' \
                 f'. ---------------------------------\n' \
                 f'\n' \
                 f'  Status variable        IPU object\n' \
                 f'. ---------------------------------\n' \
                 f'\n' \
                 f'  Indication variable    COS object\n' \
                 f'. ---------------------------------\n' \
                 f'  S_CC                   {cur_name:19} \n' \
                 f'  S_TC                   {cur_name:19} \n' \
                 f'\n' \
                 f'\n'

        total_all.append(total)

print()
print('Начинаю запись в файл')
print()

with open('out.txt', 'w', encoding='utf8') as f:
    for text in total_all:
        f.write(text)

print('Генерация и запись в файл закончены!')
print('Ошибки не искались и не фиксировались!!!')