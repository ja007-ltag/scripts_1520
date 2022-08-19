import string

FILE_IN = "list_in"  # список IPU объектов в столбик
FILE_OUT_FULL = "list_out_full"  # полная копия файла с отметками об ошибках
FILE_OUT_ERR = "list_out_err"  # только ошибочные строки
FILE_LIST_EXCEPTIONS = "list_exceptions"  # список игнорируемых строк

STR_ASCII = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
STR_NUM = string.digits  # '0123456789'
STR_SIMBOLS = '_'
STR_CHECK = f'{STR_ASCII}{STR_NUM}{STR_SIMBOLS}'


# True, если строка состоит из STR_ASCII, STR_NUM, STR_SIMBOLS
# или пустая
def string_check(line_string: str):
    for char in line_string:
        if char not in STR_CHECK:
            return False
    return True


# False - если в строке имеются "кривые символы"
def check_simbols(line_string: str):
    for char in line_string:
        if not char.isalnum() and char not in STR_SIMBOLS:
            return False
    return True


# True - если в строке имеются символы в нижнем регистре
def check_lower(line_string: str):
    for char in line_string:
        if char.islower():
            return True
    return False


if __name__ == '__main__':
    with open(FILE_IN, "r", encoding='utf-8') as file:
        list_line_in = [line.strip() for line in file]

    with open(FILE_LIST_EXCEPTIONS, "r", encoding='utf-8') as file:
        list_exceptions = [line.strip() for line in file]

    print(list_line_in)
    print(list_exceptions)

    list_line_out_full = []
    list_line_out_err = []

    for line in list_line_in:
        if string_check(line) or line in list_exceptions:
            list_line_out_full.append(line)
            continue

        line_full = f'{line:15} - ERROR'
        line_err = f'> {line}'

        if not line.isascii():
            line_full = f'{line_full} - find RUS'

        if not check_simbols(line):
            line_full = f'{line_full} - BAD SYMBOLS'

        if check_lower(line):
            line_full = f'{line_full} - lower case'

        list_line_out_full.append(line_full)
        list_line_out_err.append(line_err)

    with open(FILE_OUT_FULL, "w", encoding='utf-8') as file:
        file.writelines(f'{line}\n' for line in list_line_out_full)

    with open(FILE_OUT_ERR, "w", encoding='utf-8') as file:
        file.writelines(f'{line}\n' for line in list_line_out_err)
