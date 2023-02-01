def print_saut_ok(name, address):
    def line2(s1, s2, x0=4, x1=31):
        return f".{' ':4}{s1:31} {s2}"

    def line3(s1, s2, s3):
        return f".{' ':4}{s1:31} {s2:15} ({s3})"

    text = list()

    text.append('.')
    text.append(line2('Controller:', f'SAUT_{name}'))
    text.append(line2('Address:', f'0X{address}'))
    text.append(line2('Type:', '"Controller_SAUT-1.0", 0X04'))
    text.append(line2('Converter:', 'PCU_SAUT'))

    text.append(line3('GPUTYPE', f'R_TYPE_{name}', 'SAUT_GPU_TYPE'))
    text.append(line3('GPUPED', f'R_PED_{name}', 'SAUT_PED'))
    text.append(line3('GPUNUM', f'R_NUM_{name}', 'SAUT_GPU_NUM'))
    text.append(line3('GPUPER1', f'R_PER1_{name}', 'SAUT_STAGE'))
    text.append(line3('GPUPER2', f'R_PER2_{name}', 'SAUT_STAGE'))
    text.append(line3('GPUPER3', f'R_PER3_{name}', 'SAUT_STAGE'))
    text.append(line3('GPUROUT', f'R_ROUT_{name}', 'SAUT_ROUTE'))
    text.append(line3('GPUSTAT', f'A_STAT_{name}', 'SAUT_GPUSTAT'))
    text.append(line3('GPUCURR', f'A_CURR_{name}', 'SAUT_GPUCURR'))
    text.append(line3('GPUCODE', f'A_CODE_{name}', 'SAUT_GPUCODE'))
    text.append(line3('GPULINE', f'A_LINE_{name}', 'SAUT_GPULINE'))
    text.append('.' * 125)

    return '\n'.join(text)


def print_saut_id_ipu(name):
    def line2(s1, s2):
        return f".{' ':2}{s1:15} {'-':5} {s2:22} {'-':11} {'-':10}"

    text = list()
    text.append(line2(f'R_TYPE_{name}', 'SAUT_GPU_TYPE'))
    text.append(line2(f'R_PED_{name}', 'SAUT_PED'))
    text.append(line2(f'R_NUM_{name}', 'SAUT_GPU_NUM'))
    text.append(line2(f'R_PER1_{name}', 'SAUT_STAGE'))
    text.append(line2(f'R_PER2_{name}', 'SAUT_STAGE'))
    text.append(line2(f'R_PER3_{name}', 'SAUT_STAGE'))
    text.append(line2(f'R_ROUT_{name}', 'SAUT_ROUTE'))
    text.append(line2(f'A_STAT_{name}', 'SAUT_GPUSTAT'))
    text.append(line2(f'A_CURR_{name}', 'SAUT_GPUCURR'))
    text.append(line2(f'A_CODE_{name}', 'SAUT_GPUCODE'))
    text.append(line2(f'A_LINE_{name}', 'SAUT_GPULINE'))
    text.append('')

    return '\n'.join(text)


def print_saut_id_log(name, leg0_neighbour=('NONE', '0'), leg1_neighbour=('NONE', '0')):
    def line_name(s1, type='SAUT_NSP'):
        return f"{' ':2}External name: {s1:19} Type: {type:14} "

    def line2(s1, s2):
        return f"{' ':2}{s1:22} {s2:19} "

    text = [
        line_name(f'AB_{name}'),
        f"{'. ':=<58}",
        '',
        '  Leg:   Neighbour:      Neighbours leg:',
        f"{'. ':-<40}",
        f"{'0':>6} {leg0_neighbour[0]:>12} {leg0_neighbour[1]:>20}",
        f"{'1':>6} {leg1_neighbour[0]:>12} {leg1_neighbour[1]:>20}",
        '',
        '  Individualizations',
        f"{'. ':-<20}",
        '  I_AB=0       I_NUM=0      I_PER=0      I_SAUT=0     I_SIG=0      ',
        '  I_TYPE=0     I_T_VKL=5    I_VKL=0      ',
        '',
        '  Order variable   Logical object  Status variable',
        f"{'. ':-<58}",
        '',
        '  Order variable         IPU object',
        f"{'. ':-<35}",
        line2('O_NUM', f'R_NUM_{name}'),
        line2('O_PED', f'R_PED_{name}'),
        line2('O_PER1', f'R_PER1_{name}'),
        line2('O_PER2', f'R_PER2_{name}'),
        line2('O_PER3', f'R_PER3_{name}'),
        line2('O_ROUT', f'R_ROUT_{name}'),
        line2('O_TYPE', f'R_TYPE_{name}'),
        '',
        '  Status variable        IPU object',
        f"{'. ':-<35}",
        line2('C_CODE', f'A_CODE_{name}'),
        line2('C_CURR', f'A_CURR_{name}'),
        line2('C_LINE', f'A_LINE_{name}'),
        line2('C_STAT', f'A_STAT_{name}'),
        '',
        '  Indication variable    COS object',
        f"{'. ':-<35}",
        line2('S_CODE', f'AB_{name}'),
        line2('S_CURR', f'AB_{name}'),
        line2('S_LINE', f'AB_{name}'),
        line2('S_STAT', f'AB_{name}'),
        '',
        '',
    ]

    text = [f'.{line}' for line in text]

    return '\n'.join(text)


# print(print_saut_ok('3N', 'D203'))
# print(print_saut_id_ipu('3N'))
# print(print_saut_id_log('3N'))

with open('in_saut.txt', 'r') as f:
    in_saut_list = [s.strip().upper() for s in f if s.strip()]

out_list_ok = []
out_list_id_ipu = []
out_list_id_log = []

for s in in_saut_list:
    s = s.split()
    cur_address = ''.join(s[:2])
    cur_name = s[2]

    cur_leg0 = cur_leg1 = ('NONE', '0')
    if len(s) == 7:
        cur_leg0 = tuple(s[3:5])
        cur_leg1 = tuple(s[5:])

    out_list_ok.append(print_saut_ok(name=cur_name, address=cur_address))
    out_list_id_ipu.append(print_saut_id_ipu(name=cur_name))
    out_list_id_log.append(print_saut_id_log(name=cur_name, leg0_neighbour=cur_leg0, leg1_neighbour=cur_leg1))

pcu_saut = '\n'.join([
    f'.',
    f'.    Converter:                      PCU_SAUT',
    f'.    Appearance:                     Redundant',
    f'.    Location:                       "Reutovo_SAUT"',
    f'.    Type:                           Pcu128',
    f'{"":.<125}',
])
out_list_ok.append(pcu_saut)

with open('out_saut_ok.txt', 'w', encoding='utf8') as f:
    for text in out_list_ok: f.write(f'{text}\n')

with open('out_saut_id_ipu.txt', 'w', encoding='utf8') as f:
    for text in out_list_id_ipu: f.write(f'{text}\n')

with open('out_saut_id_log.txt', 'w', encoding='utf8') as f:
    for text in out_list_id_log: f.write(f'{text}\n')

    # print(print_saut_id_log(name=cur_name, leg0_neighbour=cur_leg0, leg1_neighbour=cur_leg1))

    # print(f'{s}, {cur_address = }, {cur_name = }, {len(s) = }, {cur_leg0 = }, {cur_leg1 = }')

print(in_saut_list)
