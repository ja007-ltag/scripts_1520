list_ok = """

ГКЕН-Е	2PGER				0X28A1
ГКЕН-Е	B2APGER				0X28A9
ГКЕН-Е	48ASGER				0X28AB
ОКД-Е-В	STALEN_OKD_EV_RK15	0X28AD


ГКЕН-Е	2NAPGER				0X28C1
ГКЕН-Е	27ASGER				0X28C5

ГКЕН-Е	2APGEP				0X28Е1
ГКЕН-Е	17SGEP				0X28Е9

ГКЕН-Е	20SGEP				0X2615

"""

# ['ГКЛС-Е', '1_1GK_PIT', '0X2СА1']
all_list = [line.split() for line in list_ok.split('\n') if line != '']

print(all_list)

list_gkls_e = []
list_gkls_e_int_data = []
list_gkls_e_int_data_for_line = []
list_gkls_e_int_data_IPU_objects = []

list_gken_e = []
list_gken_e_int_data = []
list_gken_e_int_data_for_line = []
list_gken_e_int_data_IPU_objects = []

# list_okd_e = []
# list_okd_ev = []

for cur_line in all_list:
    type_ok, name, address_ok = cur_line

    if type_ok == 'ГКЛС-Е':
        text_ok = f'    Controller:         GEN_{name}\n' \
                  f'    Address:            {address_ok}\n' \
                  f'    Type:               "Controller_STALEN-1.4", 0x06\n' \
                  f'    Converter:          PCU_REAL_STALEN_ALSO_ELP2\n' \
                  f'\n' \
                  f'    CODE                {f"G_CODE_{name}":27} (STALEN_CODE)\n' \
                  f'    K                   {f"G_K_{name}":27} (STALEN_K)\n' \
                  f'\n' \
                  f'    F                   {f"G_F_{name}":27} (STALEN_F)\n' \
                  f'    SYN                 {f"G_SYN_{name}":27} (STALEN_SYN)\n' \
                  f'    KPT                 {f"G_KPT_{name}":27} (STALEN_KPT)\n' \
                  f'    GM                  {f"G_GM_{name}":27} (STALEN_GM)\n' \
                  f'    IN                  {f"G_IN_{name}":27} (STALEN_IN)\n' \
                  f'    SRM                 {f"G_RM_{name}":27} (STALEN_RM)\n' \
                  f'    L                   {f"G_L_{name}":27} (STALEN_VAL)\n' \
                  f'    I                   {f"G_I_{name}":27} (STALEN_I)\n' \
                  f'    GALSSTAT1           {f"GALSST_O_{name}":27} (STALEN_CHAN)\n' \
                  f'    GALSSTAT2           {f"GALSST_R_{name}":27} (STALEN_CHAN)\n' \
                  f'{"." * 125}\n' \
                  f'\n'

        text_int_data = f'  External name: {f"GEN_{name}":20} Type: STALEN_GKLS   \n' \
                        f'. ========================================================\n' \
                        f'\n' \
                        f'  Leg:   Neighbour:      Neighbours leg:\n' \
                        f'. --------------------------------------\n' \
                        f'\n' \
                        f'  Individualizations\n' \
                        f'. ------------------\n' \
                        f'  I_KPT=5      I_DIR=0      I_SYN=1      \n' \
                        f'\n' \
                        f'  Order variable   Logical object  Status variable\n' \
                        f'. --------------------------------------------------------\n' \
                        f'\n' \
                        f'  Order variable         IPU object\n' \
                        f'. ---------------------------------\n' \
                        f'  O_L                    {f"G_L_{name}":19} \n' \
                        f'  O_F                    {f"G_F_{name}":19} \n' \
                        f'  O_SYN                  {f"G_SYN_{name}":19} \n' \
                        f'  O_KPT                  {f"G_KPT_{name}":19} \n' \
                        f'  O_GM                   {f"G_GM_{name}":19} \n' \
                        f'  O_IN                   {f"G_IN_{name}":19} \n' \
                        f'\n' \
                        f'  Status variable        IPU object\n' \
                        f'. ---------------------------------\n' \
                        f'  C_L                    {f"G_L_{name}":19} \n' \
                        f'  C_I                    {f"G_I_{name}":19} \n' \
                        f'  C_F                    {f"G_F_{name}":19} \n' \
                        f'  C_SYN                  {f"G_SYN_{name}":19} \n' \
                        f'  C_KPT                  {f"G_KPT_{name}":19} \n' \
                        f'  C_IN                   {f"G_IN_{name}":19} \n' \
                        f'  C_RM                   {f"G_RM_{name}":19} \n' \
                        f'  C_GM                   {f"G_GM_{name}":19} \n' \
                        f'  C_STATE1               {f"GALSST_O_{name}":19} \n' \
                        f'  C_STATE2               {f"GALSST_R_{name}":19} \n' \
                        f'\n' \
                        f'  Indication variable    COS object\n' \
                        f'. ---------------------------------\n' \
                        f'  S_L                    {f"GEN_{name}":19} \n' \
                        f'  S_I                    {f"GEN_{name}":19} \n' \
                        f'  S_SYN                  {f"GEN_{name}":19} \n' \
                        f'  S_KPT                  {f"GEN_{name}":19} \n' \
                        f'  S_F                    {f"GEN_{name}":19} \n' \
                        f'  S_IN                   {f"GEN_{name}":19} \n' \
                        f'  S_RM                   {f"GEN_{name}":19} \n' \
                        f'  S_GM                   {f"GEN_{name}":19} \n' \
                        f'  S_STATE1               {f"GEN_{name}":19} \n' \
                        f'  S_STATE2               {f"GEN_{name}":19} \n' \
                        f'\n' \
                        f'\n'

        text_int_data_for_line = f'  {"O_CODE":22} {f"G_CODE_{name}":19} \n' \
                                 f'  {"O_K":22} {f"G_K_{name}":19} \n' \
                                 f'\n' \
                                 f'  {"C_CODE":22} {f"G_CODE_{name}":19} \n' \
                                 f'  {"C_K":22} {f"G_K_{name}":19} \n' \
                                 f'\n'

        text_int_data_IPU_objects = f'  {f"G_CODE_{name}":23} -   {"STALEN_CODE":22} -           -         \n' \
                                    f'  {f"G_K_{name}":23} -   {"STALEN_K":22} -           -         \n' \
                                    f'  {f"G_F_{name}":23} -   {"STALEN_F":22} -           -         \n' \
                                    f'  {f"G_SYN_{name}":23} -   {"STALEN_SYN":22} -           -         \n' \
                                    f'  {f"G_KPT_{name}":23} -   {"STALEN_KPT":22} -           -         \n' \
                                    f'  {f"G_GM_{name}":23} -   {"STALEN_GM":22} -           -         \n' \
                                    f'  {f"G_IN_{name}":23} -   {"STALEN_IN":22} -           -         \n' \
                                    f'  {f"G_RM_{name}":23} -   {"STALEN_RM":22} -           -         \n' \
                                    f'  {f"G_L_{name}":23} -   {"STALEN_VAL":22} -           -         \n' \
                                    f'  {f"G_I_{name}":23} -   {"STALEN_I":22} -           -         \n' \
                                    f'  {f"GALSST_O_{name}":23} -   {"STALEN_CHAN":22} -           -         \n' \
                                    f'  {f"GALSST_R_{name}":23} -   {"STALEN_CHAN":22} -           -         \n' \
                                    f'\n'

        list_gkls_e.append(text_ok)
        list_gkls_e_int_data.append(text_int_data)
        list_gkls_e_int_data_for_line.append(text_int_data_for_line)
        list_gkls_e_int_data_IPU_objects.append(text_int_data_IPU_objects)


    if type_ok == 'ГКЕН-Е':
        text_ok = f'    Controller:         GKEN_{name}\n' \
                  f'    Address:            {address_ok}\n' \
                  f'    Type:               "Controller_STALEN-1.4", 0x09\n' \
                  f'    Converter:          PCU_REAL_STALEN_ALSO_ELP2\n' \
                  f'\n' \
                  f'    SC1                 {f"R_SC1_GKEN_{name}":27} (STALEN_SC)\n' \
                  f'    SC2                 {f"R_SC2_GKEN_{name}":27} (STALEN_SC)\n' \
                  f'    L                   {f"R_L_GKEN_{name}":27} (STALEN_L8)\n' \
                  f'    SM                  {f"R_SM_GKEN_{name}":27} (STALEN_SM)\n' \
                  f'    CM                  {f"R_CM_GKEN_{name}":27} (STALEN_CM)\n' \
                  f'    GM                  {f"R_GM_GKEN_{name}":27} (STALEN_GM)\n' \
                  f'    IN                  {f"R_IN_GKEN_{name}":27} (STALEN_IN)\n' \
                  f'\n' \
                  f'    STATE1              {f"SPC_ST1_GKEN_{name}":27} (STALEN_CHAN)\n' \
                  f'    STATE2              {f"SPC_ST2_GKEN_{name}":27} (STALEN_CHAN)\n' \
                  f'\n' \
                  f'    RM                  {f"S_RM_GKEN_{name}":27} (STALEN_RM)\n' \
                  f'{"." * 125}\n' \
                  f'\n'

        text_int_data = f'  External name: {f"GKEN_{name}":20} Type: STALEN_GKEN   \n' \
                        f'. ========================================================\n' \
                        f'\n' \
                        f'  Leg:   Neighbour:      Neighbours leg:\n' \
                        f'. --------------------------------------\n' \
                        f'\n' \
                        f'  Individualizations\n' \
                        f'. ------------------\n' \
                        f'  I_ROUT=0     \n' \
                        f'\n' \
                        f'  Order variable   Logical object  Status variable\n' \
                        f'. --------------------------------------------------------\n' \
                        f'\n' \
                        f'  Order variable         IPU object\n' \
                        f'. ---------------------------------\n' \
                        f'  O_L                    {f"R_L_GKEN_{name}":19} \n' \
                        f'  O_SM                   {f"R_SM_GKEN_{name}":19} \n' \
                        f'  O_GM                   {f"R_GM_GKEN_{name}":19} \n' \
                        f'  O_IN                   {f"R_IN_GKEN_{name}":19} \n' \
                        f'\n' \
                        f'  Status variable        IPU object\n' \
                        f'. ---------------------------------\n' \
                        f'  C_SC1                  {f"R_SC1_GKEN_{name}":19} \n' \
                        f'  C_SC2                  {f"R_SC2_GKEN_{name}":19} \n' \
                        f'  C_L                    {f"R_L_GKEN_{name}":19} \n' \
                        f'  C_CM                   {f"R_CM_GKEN_{name}":19} \n' \
                        f'  C_SM                   {f"R_SM_GKEN_{name}":19} \n' \
                        f'  C_GM                   {f"R_GM_GKEN_{name}":19} \n' \
                        f'  C_IN                   {f"R_IN_GKEN_{name}":19} \n' \
                        f'  C_RM                   {f"S_RM_GKEN_{name}":19} \n' \
                        f'  C_STATE1               {f"SPC_ST1_GKEN_{name}":19} \n' \
                        f'  C_STATE2               {f"SPC_ST2_GKEN_{name}":19} \n' \
                        f'\n' \
                        f'  Indication variable    COS object\n' \
                        f'. ---------------------------------\n' \
                        f'  S_SC1                  {f"GKEN_{name}":19} \n' \
                        f'  S_SC2                  {f"GKEN_{name}":19} \n' \
                        f'  S_L                    {f"GKEN_{name}":19} \n' \
                        f'  S_SM                   {f"GKEN_{name}":19} \n' \
                        f'  S_GM                   {f"GKEN_{name}":19} \n' \
                        f'  S_IN                   {f"GKEN_{name}":19} \n' \
                        f'  S_RM                   {f"GKEN_{name}":19} \n' \
                        f'  S_STATE1               {f"GKEN_{name}":19} \n' \
                        f'  S_STATE2               {f"GKEN_{name}":19} \n' \
                        f'  S_CM                   {f"GKEN_{name}":19} \n' \
                        f'\n' \
                        f'\n'

        text_int_data_for_line = f'  O_SC1                  {f"R_SC1_GKEN_{name}":19} \n' \
                                 f'  O_SC2                  {f"R_SC2_GKEN_{name}":19} \n' \
                                 f'  O_CM                   {f"R_CM_GKEN_{name}":19} \n' \
                                 f'\n'

        text_int_data_IPU_objects = f'  {f"R_SC1_GKEN_{name}":23} -   STALEN_SC             -           -         \n' \
                                    f'  {f"R_SC2_GKEN_{name}":23} -   STALEN_SC             -           -         \n' \
                                    f'  {f"R_L_GKEN_{name}":23} -   STALEN_L8             -           -         \n' \
                                    f'  {f"R_SM_GKEN_{name}":23} -   STALEN_SM             -           -         \n' \
                                    f'  {f"R_CM_GKEN_{name}":23} -   STALEN_CM             -           -         \n' \
                                    f'  {f"R_GM_GKEN_{name}":23} -   STALEN_GM             -           -         \n' \
                                    f'  {f"R_IN_GKEN_{name}":23} -   STALEN_IN             -           -         \n' \
                                    f'  {f"S_RM_GKEN_{name}":23} -   STALEN_RM             -           -         \n' \
                                    f'  {f"SPC_ST1_GKEN_{name}":23} -   STALEN_CHAN           -           -         \n' \
                                    f'  {f"SPC_ST2_GKEN_{name}":23} -   STALEN_CHAN           -           -         \n' \
                                    f'\n'

        list_gken_e.append(text_ok)
        list_gken_e_int_data.append(text_int_data)
        list_gken_e_int_data_for_line.append(text_int_data_for_line)
        list_gken_e_int_data_IPU_objects.append(text_int_data_IPU_objects)

with open('out_stalen_OC_gkls.txt', 'w', encoding='utf8') as f:
    for text in list_gkls_e:
        f.write(text)

with open('out_stalen_ID_gkls.txt', 'w', encoding='utf8') as f:
    for text in list_gkls_e_int_data:
        f.write(text)

# list_gkls_e_int_data_for_line.sort()
# with open('out_stalen_ID_gkls_for_line.txt', 'w', encoding='utf8') as f:
#     for text in list_gkls_e_int_data_for_line:
#         f.write(text)

with open('out_stalen_ID_gkls_IPU_objects.txt', 'w', encoding='utf8') as f:
    for text in list_gkls_e_int_data_IPU_objects:
        f.write(text)



with open('out_stalen_OC_gken.txt', 'w', encoding='utf8') as f:
    for text in list_gken_e:
        f.write(text)

with open('out_stalen_ID_gken.txt', 'w', encoding='utf8') as f:
    for text in list_gken_e_int_data:
        f.write(text)

# list_gken_e_int_data_for_line.sort()
# with open('out_stalen_ID_gken_for_line.txt', 'w', encoding='utf8') as f:
#     for text in list_gken_e_int_data_for_line:
#         f.write(text)

with open('out_stalen_ID_gken_IPU_objects.txt', 'w', encoding='utf8') as f:
    for text in list_gken_e_int_data_IPU_objects:
        f.write(text)


# print(*list_gken_e_int_data_for_line, sep='')
list_gkls_e_int_data_for_line.sort()
list_gken_e_int_data_for_line.sort()

print(list_gkls_e_int_data_for_line[:1])
print(list_gken_e_int_data_for_line[:1])

print(len(list_gkls_e_int_data_for_line))
print(len(list_gken_e_int_data_for_line))
print()

list_GKLS_and_GKEN = []
for text_gkls,text_gken in zip(list_gkls_e_int_data_for_line, list_gken_e_int_data_for_line):
    text_gkls = text_gkls.split('\n\n')
    text = f'{text_gkls[0]}\n{text_gken}{text_gkls[1]}\n' \
           f'{"-" * 80}' \
           f'\n'
    list_GKLS_and_GKEN.append(text)

list_GKLS_and_GKEN.sort(
    key=lambda x: (int(x.split()[1].split('_')[3])
                   if (x.split()[1].split('_')[3]).isdigit()
                   else int(x.split()[1].split('_')[3][:-2]))
)
with open('out_stalen_ID_for_line.txt', 'w', encoding='utf8') as f:
    for text in list_GKLS_and_GKEN:
        f.write(text)
