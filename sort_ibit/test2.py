list_ibit = ['I_CALLON=100', 'I_CC=50', 'I_DIR=0', 'I_IND=0', 'I_TC=0', 'I_TC_LZF=0', 'I_I=1']

# I_CALLON=100 I_CC=50      I_DIR=0      I_IND=0      I_TC=0       I_TC_LZF=0
temp_str = ''
for index, value in enumerate(list_ibit):
    if index % 5 == 0:
        if temp_str == '':
            temp_str += f'  {value:13}'
        else:
            temp_str += f'\n  {value:13}'
    else:
        temp_str += f'{value:13}'

print(temp_str)
print(type(temp_str))




    # temp_str += f'{value:13}'


#   I_CALLON=100 I_CC=50      I_DIR=0      I_IND=0      I_TC=0
#   I_TC_LZF=0

