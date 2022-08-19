# Прямое копирование файла построчно
# with open("Interlocking_data_in", "r", encoding="utf-8") as file_input:
#     with open('Interlocking_data_out', 'w', encoding='utf-8') as file_output:
#         for line in file_input:
#             file_output.writelines(line)


int_data = []
with open("Interlocking_data_in", "r", encoding="utf-8") as file_input:
    for line in file_input:
        int_data.append(line)

# text = ''.join(int_data)
# print(text)

count_line = 0
find_ibit = False
list_ibit = []

for line in int_data:
    count_line += 1

    # если строка начинается с комментария
    # или строка пустая, то должны перейти к следующей строке
    if line[0] == '.' or line.isspace():
        continue

    if 'Individualizations' in line:
        find_ibit = True
        print(f'{count_line = }')
        continue

    if find_ibit and '=' in line:
        cur_line = line.replace(' =', '=').replace('= ', '=')
        cur_line = cur_line.split()
        list_ibit.extend(cur_line)
        continue

    # find_ibit and "Нашли ключевое слово",
    # и должны остановиться,
    # чтобы обработать список айбитов,
    # т.е. отсортировать и его обратно вставить в главный список int_data
    if find_ibit and 'Order variable' in line:
        # Сортируем список
        list_ibit.sort()
        print(list_ibit)

        for cur_ibit in list_ibit:
            pass


        # Мы должны обнулить переменные в самом конце
        find_ibit = False
        list_ibit = []


# Запомнить номера строк, откуда брать i-биты,
# чтобы потом понимать, куда вставить эти i-биты

# with open('Interlocking_data_out', 'w', encoding='utf-8') as file_output:
#     for line in int_data:
#         file_output.writelines(line)
