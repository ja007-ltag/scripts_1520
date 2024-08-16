"""
Генерация имеется только для ОК ГКЛС-Е и ГКЕН-Е

Для ОКД-Е-В не делалось, это проще руками добавить пару генераторов.
"""

list_ok = """
STALEN_GKEN_5_55ASGER	09	16	65	IPU_GATE_V1_V2		TS5_55	GKEN_5_55A_R
STALEN_GKLS_5_55ASGKR	06	16	6B	IPU_GATE_V1_V2		TS5_55	GKLS_5_55A_R

STALEN_GKEN_1CDPGEP	09	16	C1	IPU_GATE_V1_V2		TS1CDP	GKEN_1CDP_P
STALEN_GKEN_92SGEP	09	16	C3	IPU_GATE_V1_V2		TS92	GKEN_92_P
STALEN_GKEN_18SGEP	09	16	C5	IPU_GATE_V1_V2		TS18	GKEN_18_P
STALEN_GKLS_1CDPGKP	06	16	C7	IPU_GATE_V1_V2		TS1CDP	GKLS_1CDP_P
STALEN_GKLS_92SGKP	06	16	C9	IPU_GATE_V1_V2		TS92	GKLS_92_P
STALEN_GKLS_18SGKP	06	16	CB	IPU_GATE_V1_V2		TS18	GKLS_18_P

STALEN_GKEN_18_64PGEP	09	18	31	IPU_GATE_V1_V2		TS18_64P	GKEN_18_64P_P
STALEN_GKEN_64_94SGEP	09	18	33	IPU_GATE_V1_V2		TS64_94	GKEN_64_94_P
STALEN_GKEN_1BPGEP	09	18	35	IPU_GATE_V1_V2		TS1BP	GKEN_1BP_P

STALEN_GKLS_64_94SGKP	06	18	39	IPU_GATE_V1_V2		TS64_94	GKLS_64_94_P
STALEN_GKLS_1BPGKP	06	18	3B	IPU_GATE_V1_V2		TS1BP	GKLS_1BP_P

STALEN_GKEN_92ASGER	09	18	95	IPU_GATE_V1_V2		TS92	GKEN_92A_R
STALEN_GKLS_92ASGKR	06	18	9B	IPU_GATE_V1_V2		TS92	GKLS_92A_R

STALEN_GKLS_18ASGKR	06	1C	03	IPU_GATE_V1_V2		TS18	GKLS_18A_R
STALEN_GKLS_1CDPGKR	06	1C	05	IPU_GATE_V1_V2		TS1CDP	GKLS_1CDP_R

STALEN_GKEN_18ASGER	09	1C	63	IPU_GATE_V1_V2		TS18	GKEN_18A_R
STALEN_GKEN_1CDPGER	09	1C	65	IPU_GATE_V1_V2		TS1CDP	GKEN_1CDP_R
STALEN_GKEN_18_64PGER	09	1C	6B	IPU_GATE_V1_V2		TS18_64P	GKEN_18_64P_R

STALEN_GKEN_1BPGER	09	1C	C1	IPU_GATE_V1_V2		TS1BP	GKEN_1BP_R
STALEN_GKEN_1ADPGER	09	1C	C3	IPU_GATE_V1_V2		TS1ADP	GKEN_1ADP_R
STALEN_GKEN_A1PGER	09	1C	C7	IPU_GATE_V1_V2		TS1P	GKEN_A1P_R

STALEN_GKEN_1NAPGER	09	16	75	IPU_GATE_V1_V2		TS1NAP	GKEN_1NAP_R
STALEN_GKLS_1NAPGKR	06	16	7B	IPU_GATE_V1_V2		TS1NAP	GKLS_1NAP_R

STALEN_GKEN_1ADPGEP	09	16	D1	IPU_GATE_V1_V2		TS1ADP	GKEN_1ADP_P
STALEN_GKEN_1APGEP	09	16	D3	IPU_GATE_V1_V2		TS1AP	GKEN_1AP_P
STALEN_GKEN_57SGEP	09	16	D5	IPU_GATE_V1_V2		TS57	GKEN_57_P
STALEN_GKLS_1ADPGKP	06	16	D7	IPU_GATE_V1_V2		TS1ADP	GKLS_1ADP_P
STALEN_GKLS_1APGKP	06	16	D9	IPU_GATE_V1_V2		TS1AP	GKLS_1AP_P
STALEN_GKLS_57SGKP	06	16	DB	IPU_GATE_V1_V2		TS57	GKLS_57_P

STALEN_GKEN_1PGEP	09	18	41	IPU_GATE_V1_V2		TS1P	GKEN_1P_P
STALEN_GKEN_15SGEP	09	18	43	IPU_GATE_V1_V2		TS15	GKEN_15_P
STALEN_GKEN_5_55SGEP	09	18	45	IPU_GATE_V1_V2		TS5_55	GKEN_5_55_P
STALEN_GKLS_1PGKP	06	18	47	IPU_GATE_V1_V2		TS1P	GKLS_1P_P
STALEN_GKLS_15SGKP	06	18	49	IPU_GATE_V1_V2		TS15	GKLS_15_P
STALEN_GKLS_5_55SGKP	06	18	4B	IPU_GATE_V1_V2		TS5_55	GKLS_5_55_P


STALEN_GKEN_64_94ASGER	09	18	55	IPU_GATE_G1_G2		TS64_94	GKEN_64_94A_R
STALEN_GKLS_64_94ASGKR	06	18	5B	IPU_GATE_G1_G2		TS64_94	GKLS_64_94A_R

STALEN_GKLS_18_64PGKR	06	18	B3	IPU_GATE_G1_G2		TS18_64P	GKLS_18_64P_R

STALEN_GKEN_1NAPGEP	09	18	05	IPU_GATE_G1_G2		TS1NAP	GKEN_1NAP_P
STALEN_GKLS_1NAPGKP	06	18	0B	IPU_GATE_G1_G2		TS1NAP	GKLS_1NAP_P

STALEN_GKLS_18_64PGKP	06	18	C3	IPU_GATE_G1_G2		TS18_64P	GKLS_18_64P_P

STALEN_GKEN_1N1PGEP	09	1C	31	IPU_GATE_G1_G2		LN_1N1P	GKEN_1N1P_P
STALEN_GKLS_1N1PGKP	06	1C	35	IPU_GATE_G1_G2		LN_1N1P	GKLS_1N1P_P

STALEN_GKEN_1N1PGER	09	1C	91	IPU_GATE_G1_G2		LN_1N1P	GKEN_1N1P_R
STALEN_GKLS_1N1PGKR	06	1C	95	IPU_GATE_G1_G2		LN_1N1P	GKLS_1N1P_R



STALEN_GKEN_57ASGER	09	18	75	IPU_GATE_D1_D2		TS57	GKEN_57A_R
STALEN_GKLS_57ASGKR	06	18	7B	IPU_GATE_D1_D2		TS57	GKLS_57A_R

STALEN_GKLS_A1PGKR	06	18	D3	IPU_GATE_D1_D2		TS1P	GKLS_A1P_R



STALEN_GKLS_A1APGKR	06	1C	A1	IPU_GATE_D1_D2		TS1AP	GKLS_A1AP_R
STALEN_GKLS_B1APGKR	06	1C	A3	IPU_GATE_D1_D2		TS1AP	GKLS_B1AP_R
STALEN_GKLS_B1PGKR	06	1C	A5	IPU_GATE_D1_D2		TS1P	GKLS_B1P_R

STALEN_GKEN_15ASGER	09	18	85	IPU_GATE_D1_D2		TS15	GKEN_15A_R
STALEN_GKLS_15ASGKR	06	18	8B	IPU_GATE_D1_D2		TS15	GKLS_15A_R

STALEN_GKLS_57BSGKR	06	18	E3	IPU_GATE_D1_D2		TS57	GKLS_57B_R

STALEN_GKEN_A1APGER	09	1C	57	IPU_GATE_D1_D2		TS1AP	GKEN_A1AP_R
STALEN_GKEN_B1APGER	09	1C	59	IPU_GATE_D1_D2		TS1AP	GKEN_B1AP_R

STALEN_GKEN_57BSGER	09	1C	B5	IPU_GATE_D1_D2		TS57	GKEN_57B_R
STALEN_GKEN_B1PGER	09	1C	B7	IPU_GATE_D1_D2		TS1P	GKEN_B1P_R




STALEN_GKLS_1ADPGKR	06	??	??	??		TS1ADP	GKLS_1ADP_R
STALEN_GKLS_1BPGKR	06	??	??	??		TS1BP	GKLS_1BP_R
"""

# ['ГКЛС-Е', '1_1GK_PIT', '2С', 'А1']
all_list = [line.split() for line in list_ok.split('\n') if line != '']

print(*all_list, sep='\n')
print(f'Количество генераторов: {len(all_list)}')

gkls_OC = []
gkls_int_data = []
gkls_int_data_for_line = []
gkls_int_data_IPU_objects = []

gken_OC = []
gken_elbrus = []
gken_int_data = []
gken_int_data_for_line = []
gken_int_data_IPU_objects = []

# okd_e = []
# okd_ev = []

for cur_line in all_list:
    name_ok, ind_ok, A1, A2, converter, TS, name_obj = cur_line
    name = name_ok[len('STALEN_GKEN_'):]

    if ind_ok == '06':
        type_ok = 'ГКЛС-Е'
    elif ind_ok == '09':
        type_ok = 'ГКЕН-Е'
    else:
        type_ok = 'Error'
        print(f'Ошибка типа ОК в строке:\n{cur_line}')

    address_ok = A1 + A2

    if type_ok == 'ГКЛС-Е':
        text_ok = f'    Controller:         STALEN_GKLS_{name}\n' \
                  f'    Address:            0X{address_ok}\n' \
                  f'    Type:               "Controller_STALEN-1.4", 0x06\n' \
                  f'    Converter:          {converter}\n' \
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

        text_int_data = f'  External name: {f"{name_obj}":20} Type: CODE_GKLS     \n' \
                        f'. ========================================================\n' \
                        f'\n' \
                        f'  Leg:   Neighbour:      Neighbours leg:\n' \
                        f'. --------------------------------------\n' \
                        f'\n' \
                        f'  Individualizations\n' \
                        f'. ------------------\n' \
                        f'  I_L0_KJ_N1=0 I_L0_KJ_S1=0 I_L0_KJ_N2=0 I_L0_KJ_S2=0 \n' \
                        f'  I_L0_J_N1=0  I_L0_J_S1=0  I_L0_J_N2=0  I_L0_J_S2=0  I_L0_J_N3=0  I_L0_J_S3=0   \n' \
                        f'  I_L0_J_N4=0  I_L0_J_S4=0  \n' \
                        f'  I_L0_Z_N1=0  I_L0_Z_S1=0  I_L0_Z_N2=0  I_L0_Z_S2=0  I_L0_Z_N3=0  I_L0_Z_S3=0   \n' \
                        f'  I_L0_Z_N4=0  I_L0_Z_S4=0  I_L0_Z_N5=0  I_L0_Z_S5=0  \n' \
                        f'\n' \
                        f'  I_L1_KJ_N1=0 I_L1_KJ_S1=0 I_L1_KJ_N2=0 I_L1_KJ_S2=0 \n' \
                        f'  I_L1_J_N1=0  I_L1_J_S1=0  I_L1_J_N2=0  I_L1_J_S2=0  I_L1_J_N3=0  I_L1_J_S3=0   \n' \
                        f'  I_L1_J_N4=0  I_L1_J_S4=0  \n' \
                        f'  I_L1_Z_N1=0  I_L1_Z_S1=0  I_L1_Z_N2=0  I_L1_Z_S2=0  I_L1_Z_N3=0  I_L1_Z_S3=0   \n' \
                        f'  I_L1_Z_N4=0  I_L1_Z_S4=0  I_L1_Z_N5=0  I_L1_Z_S5=0  \n' \
                        f'  I_KPT=5      I_SYN=2      I_TRACK=0    \n' \
                        f'\n' \
                        f'  Order variable   Logical object  Status variable\n' \
                        f'. --------------------------------------------------------\n' \
                        f'\n' \
                        f'  Order variable         IPU object\n' \
                        f'. ---------------------------------\n' \
                        f'  O_CODE                 {f"G_CODE_{name}":19} \n' \
                        f'  O_K                    {f"G_K_{name}":19} \n' \
                        f'  O_L                    {f"G_L_{name}":19} \n' \
                        f'  O_F                    {f"G_F_{name}":19} \n' \
                        f'  O_SYN                  {f"G_SYN_{name}":19} \n' \
                        f'  O_KPT                  {f"G_KPT_{name}":19} \n' \
                        f'  O_GM                   {f"G_GM_{name}":19} \n' \
                        f'  O_IN                   {f"G_IN_{name}":19} \n' \
                        f'\n' \
                        f'  Status variable        IPU object\n' \
                        f'. ---------------------------------\n' \
                        f'  C_CODE                 {f"G_CODE_{name}":19} \n' \
                        f'  C_K                    {f"G_K_{name}":19} \n' \
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
                        f'  S_CODE                 {f"{name_obj}":19} \n' \
                        f'  S_K                    {f"{name_obj}":19} \n' \
                        f'  S_L                    {f"{name_obj}":19} \n' \
                        f'  S_I                    {f"{name_obj}":19} \n' \
                        f'  S_SYN                  {f"{name_obj}":19} \n' \
                        f'  S_KPT                  {f"{name_obj}":19} \n' \
                        f'  S_F                    {f"{name_obj}":19} \n' \
                        f'  S_IN                   {f"{name_obj}":19} \n' \
                        f'  S_RM                   {f"{name_obj}":19} \n' \
                        f'  S_GM                   {f"{name_obj}":19} \n' \
                        f'  S_STATE1               {f"{name_obj}":19} \n' \
                        f'  S_STATE2               {f"{name_obj}":19} \n' \
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

        gkls_OC.append(text_ok)
        gkls_int_data.append(text_int_data)
        gkls_int_data_for_line.append(text_int_data_for_line)
        gkls_int_data_IPU_objects.append(text_int_data_IPU_objects)

    if type_ok == 'ГКЕН-Е':
        text_ok = f'    Controller:         STALEN_GKEN_{name}\n' \
                  f'    Address:            0X{address_ok}\n' \
                  f'    Type:               "Controller_STALEN-1.4", 0x09\n' \
                  f'    Converter:          {converter}\n' \
                  f'\n' \
                  f'    SC1                 {f"R_SC1_{name}":27} (STALEN_SC)\n' \
                  f'    SC2                 {f"R_SC2_{name}":27} (STALEN_SC)\n' \
                  f'    L                   {f"R_L_{name}":27} (STALEN_L8)\n' \
                  f'    SM                  {f"R_SM_{name}":27} (STALEN_SM)\n' \
                  f'    CM                  {f"R_CM_{name}":27} (STALEN_CM)\n' \
                  f'    GM                  {f"R_GM_{name}":27} (STALEN_GM)\n' \
                  f'    IN                  {f"R_IN_{name}":27} (STALEN_IN)\n' \
                  f'\n' \
                  f'    STATE1              {f"SPC_ST1_{name}":27} (STALEN_CHAN)\n' \
                  f'    STATE2              {f"SPC_ST2_{name}":27} (STALEN_CHAN)\n' \
                  f'\n' \
                  f'    RM                  {f"S_RM_{name}":27} (STALEN_RM)\n' \
                  f'{"." * 125}\n' \
                  f'\n'

        def line_ok_el(s1, s2='', s3='', s4='2', s5='INVERT'):
            s3 = f'({s3})' if s3 != '' else ''
            s4 = f'Size: {s4}'
            s5 = f'Coding: {s5}'
            return f"  {s1:11} {s2:27} {s3:17} {s4:9} {s5}"

        text_ok_el = list()

        text_ok_el.append(f'  Controller:         STALEN_GKEN_{name}')
        text_ok_el.append(f'  Address:            0X{address_ok}')
        text_ok_el.append(f'  Type:               "Controller_STALEN-1.4", 0x09')
        text_ok_el.append(f'  Converter:          {converter}')
        text_ok_el.append('')
        text_ok_el.append('Orders')
        text_ok_el.append(line_ok_el('SC1', f'R_SC1_{name}', 'STALEN_SC', '4'))
        text_ok_el.append(line_ok_el('SC2', f'R_SC2_{name}', 'STALEN_SC', '4'))
        text_ok_el.append(line_ok_el('L', f'R_L_{name}', 'STALEN_L8', '8'))
        text_ok_el.append(line_ok_el('SM', f'R_SM_{name}', 'STALEN_SM', '2'))
        text_ok_el.append(line_ok_el('CM', f'R_CM_{name}', 'STALEN_CM', '2'))
        text_ok_el.append(line_ok_el('GM', f'R_GM_{name}', 'STALEN_GM', '2'))
        text_ok_el.append(line_ok_el('IN', f'R_IN_{name}', 'STALEN_IN', '2'))
        text_ok_el.append('')
        text_ok_el.append('Statuses')
        text_ok_el.append(line_ok_el('SC1', f'R_SC1_{name}', 'STALEN_SC', '4'))
        text_ok_el.append(line_ok_el('SC2', f'R_SC2_{name}', 'STALEN_SC', '4'))
        text_ok_el.append(line_ok_el('L', f'R_L_{name}', 'STALEN_L8', '8'))
        text_ok_el.append(line_ok_el('SM', f'R_SM_{name}', 'STALEN_SM', '2'))
        text_ok_el.append(line_ok_el('CM', f'R_CM_{name}', 'STALEN_CM', '2'))
        text_ok_el.append(line_ok_el('GM', f'R_GM_{name}', 'STALEN_GM', '2'))
        text_ok_el.append(line_ok_el('IN', f'R_IN_{name}', 'STALEN_IN', '2'))
        text_ok_el.append(line_ok_el('STATE1', f'SPC_ST1_{name}', 'STALEN_CHAN', '2'))
        text_ok_el.append(line_ok_el('STATE2', f'SPC_ST2_{name}', 'STALEN_CHAN', '2'))
        text_ok_el.append(line_ok_el('NONE', f'', '', '2'))
        text_ok_el.append(line_ok_el('RM', f'S_RM_{name}', 'STALEN_RM', '2'))
        text_ok_el.append('.' * 125)
        text_ok_el.append('')
        text_ok_el.append('')

        text_ok_el = '\n'.join(text_ok_el)

        text_int_data = f'  External name: {f"{name_obj}":20} Type: CODE_GKEN     \n' \
                        f'. ========================================================\n' \
                        f'\n' \
                        f'  Leg:   Neighbour:      Neighbours leg:\n' \
                        f'. --------------------------------------\n' \
                        f'\n' \
                        f'  Individualizations\n' \
                        f'. ------------------\n' \
                        f'  I_CM=3       I_L0_SC2=1   I_L1_SC2=0   I_SIDE=0     I_TRACK=0    \n' \
                        f'\n' \
                        f'  Order variable   Logical object  Status variable\n' \
                        f'. --------------------------------------------------------\n' \
                        f'\n' \
                        f'  Order variable         IPU object\n' \
                        f'. ---------------------------------\n' \
                        f'  O_SC1                  {f"R_SC1_{name}":19} \n' \
                        f'  O_SC2                  {f"R_SC2_{name}":19} \n' \
                        f'  O_CM                   {f"R_CM_{name}":19} \n' \
                        f'  O_L                    {f"R_L_{name}":19} \n' \
                        f'  O_SM                   {f"R_SM_{name}":19} \n' \
                        f'  O_GM                   {f"R_GM_{name}":19} \n' \
                        f'  O_IN                   {f"R_IN_{name}":19} \n' \
                        f'\n' \
                        f'  Status variable        IPU object\n' \
                        f'. ---------------------------------\n' \
                        f'  C_SC1                  {f"R_SC1_{name}":19} \n' \
                        f'  C_SC2                  {f"R_SC2_{name}":19} \n' \
                        f'  C_L                    {f"R_L_{name}":19} \n' \
                        f'  C_CM                   {f"R_CM_{name}":19} \n' \
                        f'  C_SM                   {f"R_SM_{name}":19} \n' \
                        f'  C_GM                   {f"R_GM_{name}":19} \n' \
                        f'  C_IN                   {f"R_IN_{name}":19} \n' \
                        f'  C_RM                   {f"S_RM_{name}":19} \n' \
                        f'  C_STATE1               {f"SPC_ST1_{name}":19} \n' \
                        f'  C_STATE2               {f"SPC_ST2_{name}":19} \n' \
                        f'\n' \
                        f'  Indication variable    COS object\n' \
                        f'. ---------------------------------\n' \
                        f'  S_SC1                  {f"{name_obj}":19} \n' \
                        f'  S_SC2                  {f"{name_obj}":19} \n' \
                        f'  S_CM                   {f"{name_obj}":19} \n' \
                        f'  S_L                    {f"{name_obj}":19} \n' \
                        f'  S_SM                   {f"{name_obj}":19} \n' \
                        f'  S_GM                   {f"{name_obj}":19} \n' \
                        f'  S_IN                   {f"{name_obj}":19} \n' \
                        f'  S_RM                   {f"{name_obj}":19} \n' \
                        f'  S_STATE1               {f"{name_obj}":19} \n' \
                        f'  S_STATE2               {f"{name_obj}":19} \n' \
                        f'\n' \
                        f'\n'

        text_int_data_for_line = f'  O_SC1                  {f"R_SC1_{name}":19} \n' \
                                 f'  O_SC2                  {f"R_SC2_{name}":19} \n' \
                                 f'  O_CM                   {f"R_CM_{name}":19} \n' \
                                 f'\n'

        text_int_data_IPU_objects = f'  {f"R_SC1_{name}":23} -   STALEN_SC             -           -         \n' \
                                    f'  {f"R_SC2_{name}":23} -   STALEN_SC             -           -         \n' \
                                    f'  {f"R_L_{name}":23} -   STALEN_L8             -           -         \n' \
                                    f'  {f"R_SM_{name}":23} -   STALEN_SM             -           -         \n' \
                                    f'  {f"R_CM_{name}":23} -   STALEN_CM             -           -         \n' \
                                    f'  {f"R_GM_{name}":23} -   STALEN_GM             -           -         \n' \
                                    f'  {f"R_IN_{name}":23} -   STALEN_IN             -           -         \n' \
                                    f'  {f"S_RM_{name}":23} -   STALEN_RM             -           -         \n' \
                                    f'  {f"SPC_ST1_{name}":23} -   STALEN_CHAN           -           -         \n' \
                                    f'  {f"SPC_ST2_{name}":23} -   STALEN_CHAN           -           -         \n' \
                                    f'\n'

        gken_OC.append(text_ok)
        gken_elbrus.append(text_ok_el)
        gken_int_data.append(text_int_data)
        gken_int_data_for_line.append(text_int_data_for_line)
        gken_int_data_IPU_objects.append(text_int_data_IPU_objects)

with open('out_GKLS_OC.txt', 'w', encoding='utf8', newline='\n') as f:
    for text in gkls_OC:
        f.write(text)

with open('out_GKLS_ID.txt', 'w', encoding='utf8', newline='\n') as f:
    for text in gkls_int_data:
        f.write(text)

# gkls_int_data_for_line.sort()
# with open('out_stalen_ID_gkls_for_line.txt', 'w', encoding='utf8', newline='\n') as f:
#     for text in gkls_int_data_for_line:
#         f.write(text)

with open('out_GKLS_ID_IPU_objects.txt', 'w', encoding='utf8', newline='\n') as f:
    for text in gkls_int_data_IPU_objects:
        f.write(text)

with open('out_GKEN_OC.txt', 'w', encoding='utf8', newline='\n') as f:
    for text in gken_OC:
        f.write(text)

with open('out_GKEN_OC_elbrus.txt', 'w', encoding='utf8', newline='\n') as f:
    for text in gken_elbrus:
        f.write(text)

with open('out_GKEN_ID.txt', 'w', encoding='utf8', newline='\n') as f:
    for text in gken_int_data:
        f.write(text)

# gken_int_data_for_line.sort()
# with open('out_stalen_ID_gken_for_line.txt', 'w', encoding='utf8', newline='\n') as f:
#     for text in gken_int_data_for_line:
#         f.write(text)

with open('out_GKEN_ID_IPU_objects.txt', 'w', encoding='utf8', newline='\n') as f:
    for text in gken_int_data_IPU_objects:
        f.write(text)

# print(*gken_int_data_for_line, sep='')
# gkls_int_data_for_line.sort()
# gken_int_data_for_line.sort()
#
# print(gkls_int_data_for_line[:1])
# print(gken_int_data_for_line[:1])
#
# print(len(gkls_int_data_for_line))
# print(len(gken_int_data_for_line))
# print()
# GKLS_and_GKEN = []
# for text_gkls, text_gken in zip(gkls_int_data_for_line, gken_int_data_for_line):
#     text_gkls = text_gkls.split('\n\n')
#     text = f'{text_gkls[0]}\n{text_gken}{text_gkls[1]}\n' \
#            f'{"-" * 80}' \
#            f'\n'
#     GKLS_and_GKEN.append(text)
#
# GKLS_and_GKEN.sort(
#     key=lambda x: (int(x.split()[1].split('_')[3])
#                    if (x.split()[1].split('_')[3]).isdigit()
#                    else int(x.split()[1].split('_')[3][:-2]))
# )
# with open('out_stalen_ID_for_line.txt', 'w', encoding='utf8', newline='\n') as f:
#     for text in GKLS_and_GKEN:
#         f.write(text)
