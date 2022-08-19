string='   I_APS=2   I_CALLON=3   I_DIR=0      I_IND=0'


def filter():
    list = string.split()
    string2= '     '.join(list)
    print('  ', string2)
    return string2


if "=" in string:
    filter()
