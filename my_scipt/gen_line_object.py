# Генерация объектов LINE для IntDate

line_txt = '''
0 LB1N          1
0 LN_N1P_C      1
0 LN_N3P_C      1
0 LN_N5P_C      1
0 LN_N7P_C      1
0 LN_N9P_C      1
0 LN_N11P_C     1
0 LN_N13P_C     1
0 LN_N15P_C     1
0 LN_N17P_C     1
0 LN_N19P_C     1
0 LN_N21P_C     1
0 LN_N23P_C     1
0 LN_N25P_C     1
0 LN_N27P_C     1
0 LN_N29P_C     1
0 LN_N31P_C     1
0 LN_N33P_C     1
0 LN_N35P_C     1
0 LN_N37P_C     1
1 LN_N1P_N      0
1 LN_N3P_N      0
1 LN_N5P_N      0
1 LN_N7P_N      0
1 LN_N9P_N      0
1 LN_N11P_N     0
1 LN_N13P_N     0
1 LN_N15P_N     0
1 LN_N17P_N     0
1 LN_N19P_N     0
1 LN_N21P_N     0
1 LN_N23P_N     0
1 LN_N25P_N     0
1 LN_N27P_N     0
1 LN_N29P_N     0
1 LN_N31P_N     0
1 LN_N33P_N     0
1 LN_N35P_N     0
1 LN_N37P_N     0
0 HB1N_REU_JEL  -
'''

all_objects = line_txt.strip().split('\n')
all_objects = [cur.split() for cur in all_objects]

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
                f'. --------------------------------------\n' \
                f'     {f"0 {neighbour_leg0_name:>12}":33} {neighbour_leg0_leg_num}\n' \
                f'     {f"1 {neighbour_leg1_name:>12}":33} {neighbour_leg1_leg_num}\n' \
                f'\n' \
                f'  Individualizations\n' \
                f'. ------------------\n' \
                f'  I_1UU=0      I_1ZU=0      I_2UU=0      I_2ZU=0      I_CC=50      \n' \
                f'  I_FIRST=0    I_SIG1=0     I_ZG=0       I_ZU=0       \n' \
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
                f'  S_CODE                 {cur_name:19} \n' \
                f'  S_K                    {cur_name:19} \n' \
                f'  S_TC1                  {cur_name:19} \n' \
                f'\n' \
                f'\n'

    total_all.append(total)

line_block = '''  External name: LB1N                Type: LINEBLOCK      
. ========================================================

  Leg:   Neighbour:      Neighbours leg:
. --------------------------------------
     0         SI1N                    0
     1     LN_N1P_C                    0

  Individualizations
. ------------------
  I_APS=1      I_BBS=0      I_CC=50      I_IND=0      I_IPU=0      
  I_I_OKS=0    I_LB=0       I_LB_T=2     I_LXI=0      I_PDU=0      
  I_PN=0       I_RU=1       I_SA=0       I_SAUT=0     I_SN=1       
  I_SN2=0      I_TC=1       I_UU=0       I_VI=0       I_VIP=0      
  I_DIR=0      I_LB_2000=0  I_TYPE=0     I_ITI=0      I_KVSTL=0    
  I_LXI_2=0    I_KVSTL_L=0  

  Order variable   Logical object  Status variable
. --------------------------------------------------------

  Order variable         IPU object
. ---------------------------------

  Status variable        IPU object
. ---------------------------------
  C_KJZ                  KC_C1KJ             

  Indication variable    COS object
. ---------------------------------
  SL_PK                  LB1N                
  S_BP                   LB1N                
  S_CC                   LB1N                
  S_HSP                  LB1N                
  S_LB_1IPU              LB1N                
  S_LB_2IPU              LB1N                
  S_LB_3IPU              LB1N                
  S_LB_KJZ               LB1N                
  S_LB_KPB               LB1N                
  S_LB_KPK               LB1N                
  S_LB_OZ                LB1N                
  S_LB_PJ                LB1N                


'''
total_all.insert(0, line_block)

help_block = '''  External name: HB1N_REU_JEL        Type: HELPBLOCK      
. ========================================================

  Leg:   Neighbour:      Neighbours leg:
. --------------------------------------
     0        LN_N37P_N                0

  Individualizations
. ------------------
  I_CALLON=0   I_MAK=0      I_K1=0       I_K2=0       I_K3=0       
  I_K4=0       I_K5=0       I_HB_ITI=1   

  Order variable   Logical object  Status variable
. --------------------------------------------------------

  Order variable         IPU object
. ---------------------------------

  Status variable        IPU object
. ---------------------------------

  Indication variable    COS object
. ---------------------------------
  S_CICS                 HB1N_REU_JEL        


'''
total_all.append(help_block)

print()
print('Начинаю запись в файл')
print()

with open('out_line_object.txt', 'w', encoding='utf8') as f:
    for text in total_all:
        f.write(text)

print('Генерация и запись в файл закончены!')
print('Ошибки не искались и не фиксировались!!!')
