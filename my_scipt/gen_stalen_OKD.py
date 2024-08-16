"""
Генерация для ОК ОКД-Е(ОКД) и ОКД-ЕВ

# Заполнять через tab
# name					ind		a1	a2	converter			*param
# STALEN_OKD_RK8		04		16	05	IPU_GATE_V1_V2		8
# STALEN_OKDEV_RK8		05		16	07	IPU_GATE_V1_V2		10	252


# OKDE:  *param (num_tc - количество рц)
# OKDEV: *param (num_in - количество входов, num - номер стойки)

# OKDE:  num_tc до 12 шт (PP1STAT - PP12STAT) и дополнительно 4 входа (IN13 - IN16)
# OKDEV: num_in до 16 шт (IN1 - IN16)
Данные ограничения не реализованы, (IN13 - IN16) в OKDE тоже не реализованы
"""

list_ok = """
STALEN_OKD_RK8		04	16	05	IPU_GATE_V1_V2	5
STALEN_OKDEV_RK8	05	16	07	IPU_GATE_V1_V2	10	252

STALEN_OKD_RK1		04	1C	07	IPU_GATE_V1_V2	6
STALEN_OKDEV_RK1_1	05	1C	09	IPU_GATE_V1_V2	10	283
STALEN_OKDEV_RK1_2	05	1C	0B	IPU_GATE_V1_V2	10	203

STALEN_OKDEV_RK7	05	1C	CD	IPU_GATE_V1_V2	8	242

STALEN_OKD_RK9		04	16	13	IPU_GATE_V1_V2	4
STALEN_OKDEV_RK9	05	16	15	IPU_GATE_V1_V2	10	262

STALEN_OKD_RK2		04	1C	15	IPU_GATE_V1_V2	6
STALEN_OKDEV_RK2_1	05	1C	17	IPU_GATE_V1_V2	10	293
STALEN_OKDEV_RK2_2	05	1C	19	IPU_GATE_V1_V2	10	213

STALEN_OKD_RK10		04	16	2D	IPU_GATE_G1_G2	3
STALEN_OKDEV_RK10	05	16	2F	IPU_GATE_G1_G2	10	272

STALEN_OKD_RK3		04	18	B5	IPU_GATE_G1_G2	5
STALEN_OKDEV_RK3_1	05	18	B7	IPU_GATE_G1_G2	10	303
STALEN_OKDEV_RK3_2	05	18	B9	IPU_GATE_G1_G2	10	233

STALEN_OKD_RK11		04	16	3D	IPU_GATE_G1_G2	3
STALEN_OKDEV_RK11	05	16	3F	IPU_GATE_G1_G2	10	292

STALEN_OKD_RK4		04	18	C5	IPU_GATE_G1_G2	5
STALEN_OKDEV_RK4_1	05	18	C7	IPU_GATE_G1_G2	10	313
STALEN_OKDEV_RK4_2	05	18	C9	IPU_GATE_G1_G2	10	243

STALEN_OKD_RK1A		04	1C	99	IPU_GATE_G1_G2	2
STALEN_OKDEV_RK1A_1	05	1C	9B	IPU_GATE_G1_G2	10	343
STALEN_OKDEV_RK1A_2	05	1C	9D	IPU_GATE_G1_G2	10	353

STALEN_OKD_RK12		04	16	4D	IPU_GATE_D1_D2	6
STALEN_OKDEV_RK12	05	16	4F	IPU_GATE_D1_D2	10	302

STALEN_OKD_RK5		04	18	D7	IPU_GATE_D1_D2	6
STALEN_OKDEV_RK5_1	05	18	D9	IPU_GATE_D1_D2	10	212
STALEN_OKDEV_RK5_2	05	18	DB	IPU_GATE_D1_D2	10	253

STALEN_OKD_RK13		04	1C	A7	IPU_GATE_D1_D2	6
STALEN_OKDEV_RK13	05	1C	A9	IPU_GATE_D1_D2	10	211

STALEN_OKD_RK6		04	18	E5	IPU_GATE_D1_D2	5
STALEN_OKDEV_RK6_1	05	18	E7	IPU_GATE_D1_D2	10	222
STALEN_OKDEV_RK6_2	05	18	E9	IPU_GATE_D1_D2	10	263

STALEN_OKDEV_RK15	05	1C	B9	IPU_GATE_D1_D2	8	241
"""

f_okd_oc = r'OUT_OKD\out_OKD_OC.txt'
f_okd_ipu = r'OUT_OKD\out_OKD_IPU.txt'
f_okd_cos = r'OUT_OKD\out_OKD_COS.txt'
f_okd_obj = r'OUT_OKD\out_OKD_OBJ.txt'

name_in_okdev = 'IPO IPR AVO AVR UZ DV1 DV2 PJ OK1 RK1'.split()

def ok_head(s1, s2):
    s1 = f'{s1}:' if s1[-1] != ':' else s1
    return f'    {s1:19} {s2}'

def ok_body(s1, s2, s3):
    return f'    {s1:19} {s2:27} ({s3})'

def ipu_text(s1, s2, s3='-'):
    return f'  {s1:23} -   {s2:21} {s3:11} {"-":10}'

def cos_text(s1, s2, s3='????'):
    return f'  {s1:15} {s2:13} {s3:10} '

def obj_head(name, tip):
    return f'  External name: {name:19} Type: {tip:14} '

def obj_text(s1, s2):
    return f'  {s1:22} {s2:19} '

def test():
    assert ok_head('Controller', 'STALEN_OKD_RK8') == '    Controller:         STALEN_OKD_RK8'
    assert ok_head('Controller:', 'STALEN_OKD_RK8') == '    Controller:         STALEN_OKD_RK8'

    assert (ok_body('ORES1', 'R_OKD_RK18', 'STALEN_ORES') ==
            '    ORES1               R_OKD_RK18                  (STALEN_ORES)')

    assert (ipu_text('R_OKD_RK8', 'STALEN_ORES', '-') ==
            '  R_OKD_RK8               -   STALEN_ORES           -           -         ')
    assert (ipu_text('KC_xxx', 'RELAY_STATUS_COS', 'KC_xxx') ==
            '  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         ')

    assert cos_text('KC_2N4P', 'IPUCOS', '????') == '  KC_2N4P         IPUCOS        ????       '
    assert cos_text('KC_xxx', 'IPUCOS', '????') ==  '  KC_xxx          IPUCOS        ????       '

    assert (obj_head('GEN_OKD_RK8', 'STALEN_OKD') ==
            '  External name: GEN_OKD_RK8         Type: STALEN_OKD     ')
    assert (obj_head('GEN_OKD_PK10', 'STALEN_OKDEV') ==
            '  External name: GEN_OKD_PK10        Type: STALEN_OKDEV   ')

    assert obj_text('O_ORES', 'R_OKD_RK8') == '  O_ORES                 R_OKD_RK8           '
    assert obj_text('C_STATE1', 'G_CHAN_1_OKD_RK8') == '  C_STATE1               G_CHAN_1_OKD_RK8    '

    assert gen_oc_okd_e() == """    Controller:         STALEN_OKD_RK8
    Address:            0X1605
    Type:               "Controller_STALEN-1.4", 0x04
    Converter:          IPU_GATE_V1_V2

    ORES1               R_OKD_RK8                   (STALEN_ORES)
    PP1STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP2STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP3STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP4STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP5STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP6STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP7STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP8STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP9STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP10STAT            KC_xxx                      (RELAY_STATUS_COS)

    DOCPSTAT1           G_CHAN_1_OKD_RK8            (STALEN_CHAN)
    DOCPSTAT2           G_CHAN_2_OKD_RK8            (STALEN_CHAN)
.............................................................................................................................
"""
    assert gen_oc_okd_e(name='RK8', address='1605', converter='IPU_GATE_V1_V2', num_tc=10) == """    Controller:         STALEN_OKD_RK8
    Address:            0X1605
    Type:               "Controller_STALEN-1.4", 0x04
    Converter:          IPU_GATE_V1_V2

    ORES1               R_OKD_RK8                   (STALEN_ORES)
    PP1STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP2STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP3STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP4STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP5STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP6STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP7STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP8STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP9STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP10STAT            KC_xxx                      (RELAY_STATUS_COS)

    DOCPSTAT1           G_CHAN_1_OKD_RK8            (STALEN_CHAN)
    DOCPSTAT2           G_CHAN_2_OKD_RK8            (STALEN_CHAN)
.............................................................................................................................
"""
    assert gen_oc_okd_e(name='RK8', address='1605', converter='IPU_GATE_V1_V2', num_tc=5) == """    Controller:         STALEN_OKD_RK8
    Address:            0X1605
    Type:               "Controller_STALEN-1.4", 0x04
    Converter:          IPU_GATE_V1_V2

    ORES1               R_OKD_RK8                   (STALEN_ORES)
    PP1STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP2STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP3STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP4STAT             KC_xxx                      (RELAY_STATUS_COS)
    PP5STAT             KC_xxx                      (RELAY_STATUS_COS)

    DOCPSTAT1           G_CHAN_1_OKD_RK8            (STALEN_CHAN)
    DOCPSTAT2           G_CHAN_2_OKD_RK8            (STALEN_CHAN)
.............................................................................................................................
"""

    assert gen_oc_okd_ev() == """    Controller:         STALEN_OKDEV_RK8
    Address:            0X1607
    Type:               "Controller_STALEN-1.4", 0x05
    Converter:          IPU_GATE_V1_V2

    OUT1                R_OUT1_RK8                  (STALEN_OUT)
    OUT2                R_OUT2_RK8                  (STALEN_OUT)
    OUT3                R_OUT3_RK8                  (STALEN_OUT)
    OUT4                R_OUT4_RK8                  (STALEN_OUT)
    OUT5                R_OUT5_RK8                  (STALEN_OUT)
    OUT6                R_OUT6_RK8                  (STALEN_OUT)
    OUT7                R_OUT7_RK8                  (STALEN_OUT)
    OUT8                R_OUT8_RK8                  (STALEN_OUT)
    IN1                 KC_252IPO                   (RELAY_STATUS_COS)
    IN2                 KC_252IPR                   (RELAY_STATUS_COS)
    IN3                 KC_252AVO                   (RELAY_STATUS_COS)
    IN4                 KC_252AVR                   (RELAY_STATUS_COS)
    IN5                 KC_252UZ                    (RELAY_STATUS_COS)
    IN6                 KC_252DV1                   (RELAY_STATUS_COS)
    IN7                 KC_252DV2                   (RELAY_STATUS_COS)
    IN8                 KC_252PJ                    (RELAY_STATUS_COS)
    IN9                 KC_252OK1                   (RELAY_STATUS_COS)
    IN10                KC_252RK1                   (RELAY_STATUS_COS)

    DOCPSTAT1           G_CHAN_1_OKDEV_RK8          (STALEN_CHAN)
    DOCPSTAT2           G_CHAN_2_OKDEV_RK8          (STALEN_CHAN)
.............................................................................................................................
"""
    assert gen_oc_okd_ev(name='RK8', address='1607', converter='IPU_GATE_V1_V2', num_in=10, num=252) == """    Controller:         STALEN_OKDEV_RK8
    Address:            0X1607
    Type:               "Controller_STALEN-1.4", 0x05
    Converter:          IPU_GATE_V1_V2

    OUT1                R_OUT1_RK8                  (STALEN_OUT)
    OUT2                R_OUT2_RK8                  (STALEN_OUT)
    OUT3                R_OUT3_RK8                  (STALEN_OUT)
    OUT4                R_OUT4_RK8                  (STALEN_OUT)
    OUT5                R_OUT5_RK8                  (STALEN_OUT)
    OUT6                R_OUT6_RK8                  (STALEN_OUT)
    OUT7                R_OUT7_RK8                  (STALEN_OUT)
    OUT8                R_OUT8_RK8                  (STALEN_OUT)
    IN1                 KC_252IPO                   (RELAY_STATUS_COS)
    IN2                 KC_252IPR                   (RELAY_STATUS_COS)
    IN3                 KC_252AVO                   (RELAY_STATUS_COS)
    IN4                 KC_252AVR                   (RELAY_STATUS_COS)
    IN5                 KC_252UZ                    (RELAY_STATUS_COS)
    IN6                 KC_252DV1                   (RELAY_STATUS_COS)
    IN7                 KC_252DV2                   (RELAY_STATUS_COS)
    IN8                 KC_252PJ                    (RELAY_STATUS_COS)
    IN9                 KC_252OK1                   (RELAY_STATUS_COS)
    IN10                KC_252RK1                   (RELAY_STATUS_COS)

    DOCPSTAT1           G_CHAN_1_OKDEV_RK8          (STALEN_CHAN)
    DOCPSTAT2           G_CHAN_2_OKDEV_RK8          (STALEN_CHAN)
.............................................................................................................................
"""
    assert gen_oc_okd_ev(name='RK8', address='1607', converter='IPU_GATE_V1_V2', num_in=8, num=252) == """    Controller:         STALEN_OKDEV_RK8
    Address:            0X1607
    Type:               "Controller_STALEN-1.4", 0x05
    Converter:          IPU_GATE_V1_V2

    OUT1                R_OUT1_RK8                  (STALEN_OUT)
    OUT2                R_OUT2_RK8                  (STALEN_OUT)
    OUT3                R_OUT3_RK8                  (STALEN_OUT)
    OUT4                R_OUT4_RK8                  (STALEN_OUT)
    OUT5                R_OUT5_RK8                  (STALEN_OUT)
    OUT6                R_OUT6_RK8                  (STALEN_OUT)
    OUT7                R_OUT7_RK8                  (STALEN_OUT)
    OUT8                R_OUT8_RK8                  (STALEN_OUT)
    IN1                 KC_252IPO                   (RELAY_STATUS_COS)
    IN2                 KC_252IPR                   (RELAY_STATUS_COS)
    IN3                 KC_252AVO                   (RELAY_STATUS_COS)
    IN4                 KC_252AVR                   (RELAY_STATUS_COS)
    IN5                 KC_252UZ                    (RELAY_STATUS_COS)
    IN6                 KC_252DV1                   (RELAY_STATUS_COS)
    IN7                 KC_252DV2                   (RELAY_STATUS_COS)
    IN8                 KC_252PJ                    (RELAY_STATUS_COS)

    DOCPSTAT1           G_CHAN_1_OKDEV_RK8          (STALEN_CHAN)
    DOCPSTAT2           G_CHAN_2_OKDEV_RK8          (STALEN_CHAN)
.............................................................................................................................
"""

    assert gen_ipu_okd_e() == """  R_OKD_RK8               -   STALEN_ORES           -           -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  G_CHAN_1_OKD_RK8        -   STALEN_CHAN           -           -         
  G_CHAN_2_OKD_RK8        -   STALEN_CHAN           -           -         
"""
    assert gen_ipu_okd_e(name='RK8', num_tc=10) == """  R_OKD_RK8               -   STALEN_ORES           -           -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  G_CHAN_1_OKD_RK8        -   STALEN_CHAN           -           -         
  G_CHAN_2_OKD_RK8        -   STALEN_CHAN           -           -         
"""
    assert gen_ipu_okd_e(name='RK8', num_tc=5) == """  R_OKD_RK8               -   STALEN_ORES           -           -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  KC_xxx                  -   RELAY_STATUS_COS      KC_xxx      -         
  G_CHAN_1_OKD_RK8        -   STALEN_CHAN           -           -         
  G_CHAN_2_OKD_RK8        -   STALEN_CHAN           -           -         
"""

    assert gen_ipu_okd_ev() == """\
  R_OUT1_RK8              -   STALEN_OUT            -           -         
  R_OUT2_RK8              -   STALEN_OUT            -           -         
  R_OUT3_RK8              -   STALEN_OUT            -           -         
  R_OUT4_RK8              -   STALEN_OUT            -           -         
  R_OUT5_RK8              -   STALEN_OUT            -           -         
  R_OUT6_RK8              -   STALEN_OUT            -           -         
  R_OUT7_RK8              -   STALEN_OUT            -           -         
  R_OUT8_RK8              -   STALEN_OUT            -           -         
  KC_252IPO               -   RELAY_STATUS_COS      KC_252IPO   -         
  KC_252IPR               -   RELAY_STATUS_COS      KC_252IPR   -         
  KC_252AVO               -   RELAY_STATUS_COS      KC_252AVO   -         
  KC_252AVR               -   RELAY_STATUS_COS      KC_252AVR   -         
  KC_252UZ                -   RELAY_STATUS_COS      KC_252UZ    -         
  KC_252DV1               -   RELAY_STATUS_COS      KC_252DV1   -         
  KC_252DV2               -   RELAY_STATUS_COS      KC_252DV2   -         
  KC_252PJ                -   RELAY_STATUS_COS      KC_252PJ    -         
  KC_252OK1               -   RELAY_STATUS_COS      KC_252OK1   -         
  KC_252RK1               -   RELAY_STATUS_COS      KC_252RK1   -         
  G_CHAN_1_OKDEV_RK8      -   STALEN_CHAN           -           -         
  G_CHAN_2_OKDEV_RK8      -   STALEN_CHAN           -           -         
"""
    assert gen_ipu_okd_ev(name='RK8', num_in=10, num=252) == """\
  R_OUT1_RK8              -   STALEN_OUT            -           -         
  R_OUT2_RK8              -   STALEN_OUT            -           -         
  R_OUT3_RK8              -   STALEN_OUT            -           -         
  R_OUT4_RK8              -   STALEN_OUT            -           -         
  R_OUT5_RK8              -   STALEN_OUT            -           -         
  R_OUT6_RK8              -   STALEN_OUT            -           -         
  R_OUT7_RK8              -   STALEN_OUT            -           -         
  R_OUT8_RK8              -   STALEN_OUT            -           -         
  KC_252IPO               -   RELAY_STATUS_COS      KC_252IPO   -         
  KC_252IPR               -   RELAY_STATUS_COS      KC_252IPR   -         
  KC_252AVO               -   RELAY_STATUS_COS      KC_252AVO   -         
  KC_252AVR               -   RELAY_STATUS_COS      KC_252AVR   -         
  KC_252UZ                -   RELAY_STATUS_COS      KC_252UZ    -         
  KC_252DV1               -   RELAY_STATUS_COS      KC_252DV1   -         
  KC_252DV2               -   RELAY_STATUS_COS      KC_252DV2   -         
  KC_252PJ                -   RELAY_STATUS_COS      KC_252PJ    -         
  KC_252OK1               -   RELAY_STATUS_COS      KC_252OK1   -         
  KC_252RK1               -   RELAY_STATUS_COS      KC_252RK1   -         
  G_CHAN_1_OKDEV_RK8      -   STALEN_CHAN           -           -         
  G_CHAN_2_OKDEV_RK8      -   STALEN_CHAN           -           -         
"""
    assert gen_ipu_okd_ev(name='RK8', num_in=8, num=252) == """\
  R_OUT1_RK8              -   STALEN_OUT            -           -         
  R_OUT2_RK8              -   STALEN_OUT            -           -         
  R_OUT3_RK8              -   STALEN_OUT            -           -         
  R_OUT4_RK8              -   STALEN_OUT            -           -         
  R_OUT5_RK8              -   STALEN_OUT            -           -         
  R_OUT6_RK8              -   STALEN_OUT            -           -         
  R_OUT7_RK8              -   STALEN_OUT            -           -         
  R_OUT8_RK8              -   STALEN_OUT            -           -         
  KC_252IPO               -   RELAY_STATUS_COS      KC_252IPO   -         
  KC_252IPR               -   RELAY_STATUS_COS      KC_252IPR   -         
  KC_252AVO               -   RELAY_STATUS_COS      KC_252AVO   -         
  KC_252AVR               -   RELAY_STATUS_COS      KC_252AVR   -         
  KC_252UZ                -   RELAY_STATUS_COS      KC_252UZ    -         
  KC_252DV1               -   RELAY_STATUS_COS      KC_252DV1   -         
  KC_252DV2               -   RELAY_STATUS_COS      KC_252DV2   -         
  KC_252PJ                -   RELAY_STATUS_COS      KC_252PJ    -         
  G_CHAN_1_OKDEV_RK8      -   STALEN_CHAN           -           -         
  G_CHAN_2_OKDEV_RK8      -   STALEN_CHAN           -           -         
"""
    assert gen_ipu_okd_ev(name='RK9', num_in=8, num=120) == """\
  R_OUT1_RK9              -   STALEN_OUT            -           -         
  R_OUT2_RK9              -   STALEN_OUT            -           -         
  R_OUT3_RK9              -   STALEN_OUT            -           -         
  R_OUT4_RK9              -   STALEN_OUT            -           -         
  R_OUT5_RK9              -   STALEN_OUT            -           -         
  R_OUT6_RK9              -   STALEN_OUT            -           -         
  R_OUT7_RK9              -   STALEN_OUT            -           -         
  R_OUT8_RK9              -   STALEN_OUT            -           -         
  KC_120IPO               -   RELAY_STATUS_COS      KC_120IPO   -         
  KC_120IPR               -   RELAY_STATUS_COS      KC_120IPR   -         
  KC_120AVO               -   RELAY_STATUS_COS      KC_120AVO   -         
  KC_120AVR               -   RELAY_STATUS_COS      KC_120AVR   -         
  KC_120UZ                -   RELAY_STATUS_COS      KC_120UZ    -         
  KC_120DV1               -   RELAY_STATUS_COS      KC_120DV1   -         
  KC_120DV2               -   RELAY_STATUS_COS      KC_120DV2   -         
  KC_120PJ                -   RELAY_STATUS_COS      KC_120PJ    -         
  G_CHAN_1_OKDEV_RK9      -   STALEN_CHAN           -           -         
  G_CHAN_2_OKDEV_RK9      -   STALEN_CHAN           -           -         
"""

    assert gen_cos_okd_e() == """\
  GEN_OKD_RK8     LogCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
"""
    assert gen_cos_okd_e(name='RK8', num_tc=10) == """\
  GEN_OKD_RK8     LogCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
"""
    assert gen_cos_okd_e(name='RK14', num_tc=5) == """\
  GEN_OKD_RK14    LogCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
  KC_xxx          IPUCOS        ????       
"""

    assert gen_cos_okd_ev() == """\
  GEN_OKDEV_RK8   LogCOS        ????       
  KC_252IPO       IPUCOS        ????       
  KC_252IPR       IPUCOS        ????       
  KC_252AVO       IPUCOS        ????       
  KC_252AVR       IPUCOS        ????       
  KC_252UZ        IPUCOS        ????       
  KC_252DV1       IPUCOS        ????       
  KC_252DV2       IPUCOS        ????       
  KC_252PJ        IPUCOS        ????       
  KC_252OK1       IPUCOS        ????       
  KC_252RK1       IPUCOS        ????       
"""
    assert gen_cos_okd_ev(name='RK8', num_in=10, num=252) == """\
  GEN_OKDEV_RK8   LogCOS        ????       
  KC_252IPO       IPUCOS        ????       
  KC_252IPR       IPUCOS        ????       
  KC_252AVO       IPUCOS        ????       
  KC_252AVR       IPUCOS        ????       
  KC_252UZ        IPUCOS        ????       
  KC_252DV1       IPUCOS        ????       
  KC_252DV2       IPUCOS        ????       
  KC_252PJ        IPUCOS        ????       
  KC_252OK1       IPUCOS        ????       
  KC_252RK1       IPUCOS        ????       
"""
    assert gen_cos_okd_ev(name='PK10', num_in=8, num=211) == """\
  GEN_OKDEV_PK10  LogCOS        ????       
  KC_211IPO       IPUCOS        ????       
  KC_211IPR       IPUCOS        ????       
  KC_211AVO       IPUCOS        ????       
  KC_211AVR       IPUCOS        ????       
  KC_211UZ        IPUCOS        ????       
  KC_211DV1       IPUCOS        ????       
  KC_211DV2       IPUCOS        ????       
  KC_211PJ        IPUCOS        ????       
"""

    assert gen_obj_okd_e() == """\
  External name: GEN_OKD_RK8         Type: STALEN_OKD     
. ========================================================

  Leg:   Neighbour:      Neighbours leg:
. --------------------------------------

  Individualizations
. ------------------

  Order variable   Logical object  Status variable
. --------------------------------------------------------

  Order variable         IPU object
. ---------------------------------
  O_ORES                 R_OKD_RK8           

  Status variable        IPU object
. ---------------------------------
  C_PP1                  KC_xxx              
  C_PP2                  KC_xxx              
  C_PP3                  KC_xxx              
  C_PP4                  KC_xxx              
  C_PP5                  KC_xxx              
  C_PP6                  KC_xxx              
  C_PP7                  KC_xxx              
  C_PP8                  KC_xxx              
  C_PP9                  KC_xxx              
  C_PP10                 KC_xxx              

  C_STATE1               G_CHAN_1_OKD_RK8    
  C_STATE2               G_CHAN_2_OKD_RK8    

  Indication variable    COS object
. ---------------------------------
  S_PP1                  GEN_OKD_RK8         
  S_PP2                  GEN_OKD_RK8         
  S_PP3                  GEN_OKD_RK8         
  S_PP4                  GEN_OKD_RK8         
  S_PP5                  GEN_OKD_RK8         
  S_PP6                  GEN_OKD_RK8         
  S_PP7                  GEN_OKD_RK8         
  S_PP8                  GEN_OKD_RK8         
  S_PP9                  GEN_OKD_RK8         
  S_PP10                 GEN_OKD_RK8         
  S_STAT1                GEN_OKD_RK8         
  S_STAT2                GEN_OKD_RK8         

"""
    assert gen_obj_okd_e(name='RK8', num_tc=10) == """\
  External name: GEN_OKD_RK8         Type: STALEN_OKD     
. ========================================================

  Leg:   Neighbour:      Neighbours leg:
. --------------------------------------

  Individualizations
. ------------------

  Order variable   Logical object  Status variable
. --------------------------------------------------------

  Order variable         IPU object
. ---------------------------------
  O_ORES                 R_OKD_RK8           

  Status variable        IPU object
. ---------------------------------
  C_PP1                  KC_xxx              
  C_PP2                  KC_xxx              
  C_PP3                  KC_xxx              
  C_PP4                  KC_xxx              
  C_PP5                  KC_xxx              
  C_PP6                  KC_xxx              
  C_PP7                  KC_xxx              
  C_PP8                  KC_xxx              
  C_PP9                  KC_xxx              
  C_PP10                 KC_xxx              

  C_STATE1               G_CHAN_1_OKD_RK8    
  C_STATE2               G_CHAN_2_OKD_RK8    

  Indication variable    COS object
. ---------------------------------
  S_PP1                  GEN_OKD_RK8         
  S_PP2                  GEN_OKD_RK8         
  S_PP3                  GEN_OKD_RK8         
  S_PP4                  GEN_OKD_RK8         
  S_PP5                  GEN_OKD_RK8         
  S_PP6                  GEN_OKD_RK8         
  S_PP7                  GEN_OKD_RK8         
  S_PP8                  GEN_OKD_RK8         
  S_PP9                  GEN_OKD_RK8         
  S_PP10                 GEN_OKD_RK8         
  S_STAT1                GEN_OKD_RK8         
  S_STAT2                GEN_OKD_RK8         

"""
    assert gen_obj_okd_e(name='PK10', num_tc=8) == """\
  External name: GEN_OKD_PK10        Type: STALEN_OKD     
. ========================================================

  Leg:   Neighbour:      Neighbours leg:
. --------------------------------------

  Individualizations
. ------------------

  Order variable   Logical object  Status variable
. --------------------------------------------------------

  Order variable         IPU object
. ---------------------------------
  O_ORES                 R_OKD_PK10          

  Status variable        IPU object
. ---------------------------------
  C_PP1                  KC_xxx              
  C_PP2                  KC_xxx              
  C_PP3                  KC_xxx              
  C_PP4                  KC_xxx              
  C_PP5                  KC_xxx              
  C_PP6                  KC_xxx              
  C_PP7                  KC_xxx              
  C_PP8                  KC_xxx              

  C_STATE1               G_CHAN_1_OKD_PK10   
  C_STATE2               G_CHAN_2_OKD_PK10   

  Indication variable    COS object
. ---------------------------------
  S_PP1                  GEN_OKD_PK10        
  S_PP2                  GEN_OKD_PK10        
  S_PP3                  GEN_OKD_PK10        
  S_PP4                  GEN_OKD_PK10        
  S_PP5                  GEN_OKD_PK10        
  S_PP6                  GEN_OKD_PK10        
  S_PP7                  GEN_OKD_PK10        
  S_PP8                  GEN_OKD_PK10        
  S_STAT1                GEN_OKD_PK10        
  S_STAT2                GEN_OKD_PK10        

"""

    assert gen_obj_okd_ev() == """\
  External name: GEN_OKDEV_RK8       Type: STALEN_OKDEV   
. ========================================================

  Leg:   Neighbour:      Neighbours leg:
. --------------------------------------

  Individualizations
. ------------------

  Order variable   Logical object  Status variable
. --------------------------------------------------------

  Order variable         IPU object
. ---------------------------------
  O_OUT1                 R_OUT1_RK8          
  O_OUT2                 R_OUT2_RK8          
  O_OUT3                 R_OUT3_RK8          
  O_OUT4                 R_OUT4_RK8          
  O_OUT5                 R_OUT5_RK8          
  O_OUT6                 R_OUT6_RK8          
  O_OUT7                 R_OUT7_RK8          
  O_OUT8                 R_OUT8_RK8          

  Status variable        IPU object
. ---------------------------------
  C_IN1                  KC_252IPO           
  C_IN2                  KC_252IPR           
  C_IN3                  KC_252AVO           
  C_IN4                  KC_252AVR           
  C_IN5                  KC_252UZ            
  C_IN6                  KC_252DV1           
  C_IN7                  KC_252DV2           
  C_IN8                  KC_252PJ            
  C_IN9                  KC_252OK1           
  C_IN10                 KC_252RK1           

  C_STATE1               G_CHAN_1_OKDEV_RK8  
  C_STATE2               G_CHAN_2_OKDEV_RK8  

  Indication variable    COS object
. ---------------------------------
  S_IN1                  GEN_OKDEV_RK8       
  S_IN2                  GEN_OKDEV_RK8       
  S_IN3                  GEN_OKDEV_RK8       
  S_IN4                  GEN_OKDEV_RK8       
  S_IN5                  GEN_OKDEV_RK8       
  S_IN6                  GEN_OKDEV_RK8       
  S_IN7                  GEN_OKDEV_RK8       
  S_IN8                  GEN_OKDEV_RK8       
  S_IN9                  GEN_OKDEV_RK8       
  S_IN10                 GEN_OKDEV_RK8       
  S_STATE_O              GEN_OKDEV_RK8       
  S_STATE_R              GEN_OKDEV_RK8       

"""
    assert gen_obj_okd_ev(name='RK8', num_in=10, num=252) == """\
  External name: GEN_OKDEV_RK8       Type: STALEN_OKDEV   
. ========================================================

  Leg:   Neighbour:      Neighbours leg:
. --------------------------------------

  Individualizations
. ------------------

  Order variable   Logical object  Status variable
. --------------------------------------------------------

  Order variable         IPU object
. ---------------------------------
  O_OUT1                 R_OUT1_RK8          
  O_OUT2                 R_OUT2_RK8          
  O_OUT3                 R_OUT3_RK8          
  O_OUT4                 R_OUT4_RK8          
  O_OUT5                 R_OUT5_RK8          
  O_OUT6                 R_OUT6_RK8          
  O_OUT7                 R_OUT7_RK8          
  O_OUT8                 R_OUT8_RK8          

  Status variable        IPU object
. ---------------------------------
  C_IN1                  KC_252IPO           
  C_IN2                  KC_252IPR           
  C_IN3                  KC_252AVO           
  C_IN4                  KC_252AVR           
  C_IN5                  KC_252UZ            
  C_IN6                  KC_252DV1           
  C_IN7                  KC_252DV2           
  C_IN8                  KC_252PJ            
  C_IN9                  KC_252OK1           
  C_IN10                 KC_252RK1           

  C_STATE1               G_CHAN_1_OKDEV_RK8  
  C_STATE2               G_CHAN_2_OKDEV_RK8  

  Indication variable    COS object
. ---------------------------------
  S_IN1                  GEN_OKDEV_RK8       
  S_IN2                  GEN_OKDEV_RK8       
  S_IN3                  GEN_OKDEV_RK8       
  S_IN4                  GEN_OKDEV_RK8       
  S_IN5                  GEN_OKDEV_RK8       
  S_IN6                  GEN_OKDEV_RK8       
  S_IN7                  GEN_OKDEV_RK8       
  S_IN8                  GEN_OKDEV_RK8       
  S_IN9                  GEN_OKDEV_RK8       
  S_IN10                 GEN_OKDEV_RK8       
  S_STATE_O              GEN_OKDEV_RK8       
  S_STATE_R              GEN_OKDEV_RK8       

"""
    assert gen_obj_okd_ev(name='PK10', num_in=8, num=113) == """\
  External name: GEN_OKDEV_PK10      Type: STALEN_OKDEV   
. ========================================================

  Leg:   Neighbour:      Neighbours leg:
. --------------------------------------

  Individualizations
. ------------------

  Order variable   Logical object  Status variable
. --------------------------------------------------------

  Order variable         IPU object
. ---------------------------------
  O_OUT1                 R_OUT1_PK10         
  O_OUT2                 R_OUT2_PK10         
  O_OUT3                 R_OUT3_PK10         
  O_OUT4                 R_OUT4_PK10         
  O_OUT5                 R_OUT5_PK10         
  O_OUT6                 R_OUT6_PK10         
  O_OUT7                 R_OUT7_PK10         
  O_OUT8                 R_OUT8_PK10         

  Status variable        IPU object
. ---------------------------------
  C_IN1                  KC_113IPO           
  C_IN2                  KC_113IPR           
  C_IN3                  KC_113AVO           
  C_IN4                  KC_113AVR           
  C_IN5                  KC_113UZ            
  C_IN6                  KC_113DV1           
  C_IN7                  KC_113DV2           
  C_IN8                  KC_113PJ            

  C_STATE1               G_CHAN_1_OKDEV_PK10 
  C_STATE2               G_CHAN_2_OKDEV_PK10 

  Indication variable    COS object
. ---------------------------------
  S_IN1                  GEN_OKDEV_PK10      
  S_IN2                  GEN_OKDEV_PK10      
  S_IN3                  GEN_OKDEV_PK10      
  S_IN4                  GEN_OKDEV_PK10      
  S_IN5                  GEN_OKDEV_PK10      
  S_IN6                  GEN_OKDEV_PK10      
  S_IN7                  GEN_OKDEV_PK10      
  S_IN8                  GEN_OKDEV_PK10      
  S_STATE_O              GEN_OKDEV_PK10      
  S_STATE_R              GEN_OKDEV_PK10      

"""

def gen_oc_okd_e(name='RK8', address='1605', converter='IPU_GATE_V1_V2', num_tc=10):
    res = list()

    res.append(ok_head('Controller', f'STALEN_OKD_{name}'))
    res.append(ok_head('Address', f'0X{address}'))
    res.append(ok_head('Type', f'"Controller_STALEN-1.4", 0x04'))
    res.append(ok_head('Converter', converter))

    res.append('')
    res.append(ok_body('ORES1', f'R_OKD_{name}', 'STALEN_ORES'))
    for n in range(1, num_tc + 1):
        res.append(ok_body(f'PP{n}STAT', 'KC_xxx', 'RELAY_STATUS_COS'))
    res.append('')
    res.append(ok_body('DOCPSTAT1', f'G_CHAN_1_OKD_{name}', 'STALEN_CHAN'))
    res.append(ok_body('DOCPSTAT2', f'G_CHAN_2_OKD_{name}', 'STALEN_CHAN'))
    res.append('.' * 125)
    res.append('')

    return '\n'.join(res)

def gen_oc_okd_ev(name='RK8', address='1607', converter='IPU_GATE_V1_V2', num_in=10, num=252):
    res = list()

    res.append(ok_head('Controller', f'STALEN_OKDEV_{name}'))
    res.append(ok_head('Address', f'0X{address}'))
    res.append(ok_head('Type', f'"Controller_STALEN-1.4", 0x05'))
    res.append(ok_head('Converter', converter))
    res.append('')

    # OUT-ов всегда 8
    for n in range(1, 9):
        res.append(ok_body(f'OUT{n}', f'R_OUT{n}_{name}', 'STALEN_OUT'))

    # количество IN-ов меняется
    name_list = name_in_okdev[:num_in]
    for n, s in enumerate(name_list, start=1):
        res.append(ok_body(f'IN{n}', f'KC_{num}{s}', 'RELAY_STATUS_COS'))

    res.append('')
    res.append(ok_body('DOCPSTAT1', f'G_CHAN_1_OKDEV_{name}', 'STALEN_CHAN'))
    res.append(ok_body('DOCPSTAT2', f'G_CHAN_2_OKDEV_{name}', 'STALEN_CHAN'))
    res.append('.' * 125)
    res.append('')

    return '\n'.join(res)

# IPU objects
def gen_ipu_okd_e(name='RK8', num_tc=10):
    res = list()
    res.append(ipu_text(f'R_OKD_{name}', 'STALEN_ORES', '-'))
    for n in range(1, num_tc+1):
        res.append(ipu_text('KC_xxx', 'RELAY_STATUS_COS', 'KC_xxx'))
    res.append(ipu_text(f'G_CHAN_1_OKD_{name}', 'STALEN_CHAN', '-'))
    res.append(ipu_text(f'G_CHAN_2_OKD_{name}', 'STALEN_CHAN', '-'))
    res.append('')
    return '\n'.join(res)

def gen_ipu_okd_ev(name='RK8', num_in=10, num=252):
    res = list()

    for n in range(1, 9):
        res.append(ipu_text(f'R_OUT{n}_{name}', 'STALEN_OUT', '-'))

    name_list = name_in_okdev[:num_in]
    for s in name_list:
        res.append(ipu_text(f'KC_{num}{s}', 'RELAY_STATUS_COS', f'KC_{num}{s}'))

    res.append(ipu_text(f'G_CHAN_1_OKDEV_{name}', 'STALEN_CHAN', '-'))
    res.append(ipu_text(f'G_CHAN_2_OKDEV_{name}', 'STALEN_CHAN', '-'))
    res.append('')
    return '\n'.join(res)

# COS objects
def gen_cos_okd_e(name='RK8', num_tc=10):
    res = list()
    res.append(cos_text(f'GEN_OKD_{name}', 'LogCOS'))
    for n in range(1, num_tc+1):
        res.append(cos_text('KC_xxx', 'IPUCOS'))
    res.append('')
    return '\n'.join(res)

def gen_cos_okd_ev(name='RK8', num_in=10, num=252):
    res = list()
    res.append(cos_text(f'GEN_OKDEV_{name}', 'LogCOS'))
    name_list = name_in_okdev[:num_in]
    for s in name_list:
        res.append(cos_text(f'KC_{num}{s}', 'IPUCOS'))
    res.append('')
    return '\n'.join(res)

# LOG objects
def gen_obj_okd_e(name='RK8', num_tc=10):
    name_obj = f'GEN_OKD_{name}'
    head = obj_head(name_obj,'STALEN_OKD')

    res = list()

    res.append(head)
    res.append(f'. {"=" * (len(head) - 2)}')
    res.append('')

    res.append('  Leg:   Neighbour:      Neighbours leg:')
    res.append('. --------------------------------------')
    res.append('')
    res.append('  Individualizations')
    res.append('. ------------------')
    res.append('')
    res.append('  Order variable   Logical object  Status variable')
    res.append('. --------------------------------------------------------')
    res.append('')

    res.append('  Order variable         IPU object')
    res.append('. ---------------------------------')
    res.append(obj_text('O_ORES', f'R_OKD_{name}'))
    res.append('')

    res.append('  Status variable        IPU object')
    res.append('. ---------------------------------')
    for n in range(1, num_tc+1):
        res.append(obj_text(f'C_PP{n}', f'KC_xxx'))
    res.append('')
    for n in range(1, 3):
        res.append(obj_text(f'C_STATE{n}', f'G_CHAN_{n}_OKD_{name}'))
    res.append('')

    res.append('  Indication variable    COS object')
    res.append('. ---------------------------------')

    for n in range(1, num_tc + 1):
        res.append(obj_text(f'S_PP{n}', name_obj))
    for n in range(1, 3):
        res.append(obj_text(f'S_STAT{n}', name_obj))

    res.append('')
    res.append('')
    return '\n'.join(res)

def gen_obj_okd_ev(name='RK8', num_in=10, num=252):
    name_obj = f'GEN_OKDEV_{name}'
    head = obj_head(name_obj, 'STALEN_OKDEV')

    res = list()

    res.append(head)
    res.append(f'. {"=" * (len(head) - 2)}')
    res.append('')

    res.append('  Leg:   Neighbour:      Neighbours leg:')
    res.append('. --------------------------------------')
    res.append('')
    res.append('  Individualizations')
    res.append('. ------------------')
    res.append('')
    res.append('  Order variable   Logical object  Status variable')
    res.append('. --------------------------------------------------------')
    res.append('')

    res.append('  Order variable         IPU object')
    res.append('. ---------------------------------')
    for n in range(1, 9):
        res.append(obj_text(f'O_OUT{n}', f'R_OUT{n}_{name}'))
    res.append('')

    res.append('  Status variable        IPU object')
    res.append('. ---------------------------------')
    name_list = name_in_okdev[:num_in]
    for n, s in enumerate(name_list, start=1):
        res.append(obj_text(f'C_IN{n}', f'KC_{num}{s}'))
    res.append('')
    for n in range(1,3):
        res.append(obj_text(f'C_STATE{n}', f'G_CHAN_{n}_OKDEV_{name}'))
    res.append('')

    res.append('  Indication variable    COS object')
    res.append('. ---------------------------------')
    for n in range(1, num_in + 1):
        res.append(obj_text(f'S_IN{n}', name_obj))
    res.append(obj_text('S_STATE_O', name_obj))
    res.append(obj_text('S_STATE_R', name_obj))

    res.append('')
    res.append('')
    return '\n'.join(res)

# запись в файл
def write_file(file, data):
    with open(file, 'a', encoding='utf8', newline='\n') as f:
        for text in data:
            f.write(text)

# Собственно генерация из списка исходных данных.
def generate():
    data_ok = [line for line in list_ok.split('\n') if line]

    res_ok_okd_e = res_ipu_okd_e = res_cos_okd_e = res_obj_okd_e = ''
    res_ok_okd_ev = res_ipu_okd_ev = res_cos_okd_ev = res_obj_okd_ev = ''

    for cur_ok in data_ok:
        res_ok = res_ipu = res_cos = res_obj = ''

        cur_ok = [data for data in cur_ok.split('\t') if data]
        print(cur_ok)
        names, ind, a1, a2, converter, *param = cur_ok
        address = f'{a1}{a2}'

        if ind == '04': # OKDE
            name = names[len('STALEN_OKD_'):]
            num_tc = int(param[0])

            res_ok_okd_e += gen_oc_okd_e(name=name, address=address, converter=converter, num_tc=num_tc) + '\n'
            res_ipu_okd_e += gen_ipu_okd_e(name=name, num_tc=num_tc) + '\n'
            res_cos_okd_e += gen_cos_okd_e(name=name, num_tc=num_tc)
            res_obj_okd_e += gen_obj_okd_e(name=name, num_tc=num_tc) + '\n'

        elif ind == '05': # OKDEV
            name = names[len('STALEN_OKDEV_'):]
            num_in, num = map(int, param)

            res_ok_okd_ev += gen_oc_okd_ev(name=name, address=address, converter=converter, num_in=num_in, num=num) + '\n'
            res_ipu_okd_ev += gen_ipu_okd_ev(name=name, num_in=num_in, num=num) + '\n'
            res_cos_okd_ev += gen_cos_okd_ev(name=name, num_in=num_in, num=num)
            res_obj_okd_ev += gen_obj_okd_ev(name=name, num_in=num_in, num=num) + '\n'

        else:
            print(f'ERROR!! {cur_ok}')

    res_ok = res_ok_okd_e + res_ok_okd_ev
    res_ipu = res_ipu_okd_e + res_ipu_okd_ev
    res_cos = res_cos_okd_e + res_cos_okd_ev
    res_obj = res_obj_okd_e + res_obj_okd_ev

    write_file(file=f_okd_oc, data=res_ok)
    write_file(file=f_okd_ipu, data=res_ipu)
    write_file(file=f_okd_cos, data=res_cos)
    write_file(file=f_okd_obj, data=res_obj)

if __name__ == '__main__':
    test()

    for f in f_okd_oc, f_okd_ipu, f_okd_cos, f_okd_obj:
        open(f, 'w', encoding='utf8', newline='\n').write('')

    generate()