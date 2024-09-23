from clear_ok import res as data_find

isk_obj_1520 = [
    'K1_282KP1_ALT',
    'K1_282KP2_ALT',
    'KC_282PO_ALT',
    'K1_283KP1_ALT',
    'K1_283KP2_ALT',
    'KC_283PO_ALT',
    'KC_284PO_ALT',
    'R_283PI_ALT',
    'R_282PI_ALT',
    'R_284PI_ALT',
    'K1_284KP1_ALT',
    'K1_284KP2_ALT',
]

# print(isk_obj_1520)
# фильтр данных
data_find = [obj for obj in data_find if obj not in isk_obj_1520]


# формируем из данных строку, обрезая префикс станции (4 символа в конце)
str_data = '|'.join([x[:-4] for x in data_find])

# print(str_data)

# формируем строку поиска в инт дате
str_find = f"^.*({str_data})_ALT.*\\n"
print(str_find)
print(f'{len(data_find)}')
