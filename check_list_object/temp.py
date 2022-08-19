from main import STR_SIMBOLS

list_in = [
    'Имя IPU объекта',
    'РУСС',
    'ENGLISH',
    'LowerSIMBOLS',
    'ENG_NgRM_OK',
    'ENG-ERR-SIMBOLS',
    '',
    ' ',
    'Д',
    'д',
    'U',
    'u',
    '8',
    '*',
    '_A',
    '-a',
    'asgassdggeeg_sdfasdd',
    '\n',
]


def check_simbols(line_string: str):
    for char in line_string:
        if not char.isalnum() and char not in STR_SIMBOLS:
            return False
    return True


def check_lower(line_string: str):
    for char in line_string:
        if char.islower():
            return True
    return False


for line in list_in:
    print(f'{line:15} - {check_lower(line)} ')

