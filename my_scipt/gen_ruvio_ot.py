"""
Генерация Order table для RUVIO
"""

name_order = 'O_R6'
str_var = """
RKC_PE4ZO    
RKC_PE4KO    
RKC_PE4SU    
RKC_PE4AV    
RKC_PE4PSO   
RKC_P4NK     
RKC_P4CK     
RKC_PA4K     
RK1_P3ZA     
RKC_P4ZA     
RKC_P34P     
RKC_P32P     
RKC_P12_34P  
RK1_OP12_34P 
RK1_PVPSO    
RKC_PE4SO    
RKC_N2PSS    
RKC_E2PSS    
RKC_N1PSS    
RKC_E1PSS    
RKC_PN1IR    
RKC_P91KSAO  
RKC_P101DVS  
RKC_P102VS   
RKC_1N       
RKC_1C       
RKC_2N       
RKC_2C       
RKC_A1N      
RKC_A2N      
RKC_PN2IR    
RKC_P92KSAO  
"""

list_var = str_var.split()
list_var.insert(0, name_order)

print(len(list_var))
print(list_var)

s_hider = ' | '.join(list_var)
s0 = ' | '.join([f'{0:<{len(var)}}' for var in list_var])
s1 = s0.replace('0', '1')
sep = '-' * len(s_hider)

# s_num = f'  {0:<{len(name_order)}} '

print('  Order table')
print(f'. {sep} ')
print(f'  {s_hider} ')
print(f'. {sep} ')
print(f'  {s0} ')
print(f'  {s1} ')


