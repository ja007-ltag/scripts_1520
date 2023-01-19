list_ok = """
ГКЛС-Е	1_1GK_PIT	0X2СА1
ГКЛС-Е	1_3_5GK_PIT	0X2СА3
ГКЛС-Е	1_7_9GK_PIT	0X2СА5
ГКЛС-Е	1_11_13GK_PIT	0X2СА7
ГКЛС-Е	1_15_17GK_PIT	0X2СА9
ГКЛС-Е	1_19_21GK_PIT	0X2САB

ГКЛС-Е	1_23_25GK_PIT	0X2СС1
ГКЛС-Е	1_27_29GK_PIT	0X2СС3
ГКЛС-Е	1_31_33GK_PIT	0X2СС5
ГКЛС-Е	1_35_37GK_PIT	0X2СС7

ГКЛС-Е	1_1_3GK_REL	0X2831
ГКЛС-Е	1_5_7GK_REL	0X2833
ГКЛС-Е	1_9_11GK_REL	0X2835
ГКЛС-Е	1_13_15GK_REL	0X2837
ГКЛС-Е	1_17_19GK_REL	0X2839
ОКД-Е	STALEN_OKD_E_RK1A	0X283B
ОКД-Е-В	STALEN_OKD_EV_RK1A_1	0X283D
ОКД-Е-В	STALEN_OKD_EV_RK1A_2	0X283F

ГКЛС-Е	1_21_23GK_REL	0X2851
ГКЛС-Е	1_25_27GK_REL	0X2853
ГКЛС-Е	1_29_37GK_REL	0X2855
ГКЛС-Е	1_33_35GK_REL	0X2857
ГКЛС-Е	1_37GK_REL	0X2859
ОКД-Е	STALEN_OKD_E_RK2A	0X285B
ОКД-Е-В	STALEN_OKD_EV_RK2A_1	0X285D
ОКД-Е-В	STALEN_OKD_EV_RK2A_2	0X285F

ГКЕН-Е	1_1_3GER	0X26В1
ГКЕН-Е	1_5_7GER	0X26В3
ГКЕН-Е	1_9_11GER	0X26В5
ГКЕН-Е	1_13_15GER	0X26В7
ГКЕН-Е	1_17_19GER	0X26В9
ГКЕН-Е	1_21_23GER	0X26С1
ГКЕН-Е	1_25_27GER	0X26С3
ГКЕН-Е	1_29_31GER	0X26С5
ГКЕН-Е	1_33_35GER	0X26С7
ГКЕН-Е	1_37GER	0X26С9

ГКЕН-Е	1_1GEP	0X26D1
ГКЕН-Е	1_3_5GEP	0X26D3
ГКЕН-Е	1_7_9GEP	0X26D5
ГКЕН-Е	1_11_13GEP	0X26D7
ГКЕН-Е	1_15_17GEP	0X26D9
ГКЕН-Е	1_19_21GEP	0X26DB
ГКЕН-Е	1_23_25GEP	0X26Е1
ГКЕН-Е	1_27_29GEP	0X26Е3
ГКЕН-Е	1_31_33GEP	0X26Е5
ГКЕН-Е	1_35_37GEP	0X26Е7
"""

# ['ГКЛС-Е', '1_1GK_PIT', '0X2СА1']
all_list = [line.split() for line in list_ok.split('\n') if line != '']

print(all_list)

list_gkls_e = []
list_gkls_e_int_data = []

list_gken_e = []
list_gken_e_int_data = []

# list_okd_e = []
# list_okd_ev = []

for cur_line in all_list:
    type_ok, name, address_ok = cur_line

    if type_ok == 'ГКЛС-Е':
        text_ok = f'    Controller:         GEN_{name}\n' \
                  f'    Address:            {address_ok}\n' \
                  f'    Type:               "Controller_STALEN-1.4", 0x06\n' \
                  f'    Converter:          PCU_REAL_STALEN_LINE1\n' \
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
                        f'  I_KPT=0      I_DIR=0      \n' \
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

        list_gkls_e.append(text_ok)
        list_gkls_e_int_data.append(text_int_data)

    if type_ok == 'ГКЕН-Е':
        text_ok = f'    Controller:         GKEN_{name}\n' \
                  f'    Address:            {address_ok}\n' \
                  f'    Type:               "Controller_STALEN-1.4", 0x09\n' \
                  f'    Converter:          PCU_REAL_STALEN_LINE3\n' \
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
                        f'  O_SC1                  {f"R_SC1_GKEN_{name}":19} \n' \
                        f'  O_SC2                  {f"R_SC2_GKEN_{name}":19} \n' \
                        f'  O_L                    {f"R_L_GKEN_{name}":19} \n' \
                        f'  O_CM                   {f"R_CM_GKEN_{name}":19} \n' \
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

        list_gken_e.append(text_ok)
        list_gken_e_int_data.append(text_int_data)

with open('out_stalen_OC_gkls.txt', 'w', encoding='utf8') as f:
    for text in list_gkls_e:
        f.write(text)

with open('out_stalen_ID_gkls.txt', 'w', encoding='utf8') as f:
    for text in list_gkls_e_int_data:
        f.write(text)

with open('out_stalen_OC_gken.txt', 'w', encoding='utf8') as f:
    for text in list_gken_e:
        f.write(text)

with open('out_stalen_ID_gken.txt', 'w', encoding='utf8') as f:
    for text in list_gken_e_int_data:
        f.write(text)
