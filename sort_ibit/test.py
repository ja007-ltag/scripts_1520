str_in = ['  I_CALLON=100 I_CC=50      I_DIR=0      I_IND=0      I_TC=0       \n',
          '  I_TC_LZF=0   ']

print(str_in)

str_in = str_in.replace(' =', '=').replace('= ', '=')
print(str_in.strip())

list_out = str_in.split()
print(list_out)
