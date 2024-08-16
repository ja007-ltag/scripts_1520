"""
Для быстрой замены
и генерации одинаковых объектов
"""

s = '''
  Component
. ---------
. =====================================================
. || Route | Command || Parameters || Areas | Shared ||
. =====================================================
  ||  YES  |  URAU   ||   SICM2    ||   2   |   NO   ||
. =====================================================

. ========================
. || Pretest indicators ||
. ========================
  ||                    ||
. ========================

  Main objects

. =====================================================================
. || Object | Manouevre | Seq. | Approved || Object | Seq. | Pretest ||
. =====================================================================
  || SICM2  | M_RAU = 1 |  1   |          || SICM2  |  0   |  P_RAU  ||
  || SICM2  | M_CC = 3  |  1   |          ||        |      |         ||
. =====================================================================

  Component
. ---------
. =====================================================
. || Route | Command || Parameters || Areas | Shared ||
. =====================================================
  ||  YES  |  ORAU   ||    SICM2   ||   2   |   NO   ||
. =====================================================

. ========================
. || Pretest indicators ||
. ========================
  ||                    ||
. ========================

  Main objects

. =====================================================================
. || Object | Manouevre | Seq. | Approved || Object | Seq. | Pretest ||
. =====================================================================
  || SICM2  | M_RAU = 2 |  1   |          ||        |      |         ||
  || SICM2  | M_CC = 3  |  1   |          ||        |      |         ||
. =====================================================================

'''

# цель замены (что менять в предыдущем тексте в переменной 's')
target_replace = 'SICM2'

# list_replace = [f'PT{i}' for i in (14, 16, 18, 20, 22, 24, 26, 28, 30)]
# list_replace = [f'N{i}P' for i in (30, 32, 34, 36, 38)]
# list_replace = ['TS1UP_TSM', 'TS1_5_TSM', 'TS1P_TSM', 'TS2P_TSM', 'TS2_4_TSM', 'TS2UP_TSM', 'TS3P_TSM', 'TS4P_TSM', 'TS7_TSM', 'TS6_TSM']
list_replace = 'SI1C|SIN1|SICM1|SINM1A|SINM1|SIC1A|SI1N'.split('|')
print('Список замен:')
print(list_replace)
print()

# генерация регулярных выражений для поиска логический объектов
print('Регулярные выражения для поиска логический объектов:')
print(f": ({'|'.join(list_replace)})")
print(f"YES.*SEO.*({'|'.join(list_replace)})")

result = (s.strip().replace(target_replace, name) for name in list_replace)
# for name in list_replace:
#     result.append(s.strip().replace('N2P', name))

result = '\n\n  '.join(result)
# print(f'  {result}\n\n')

with open('out_replace.txt', 'w', encoding='utf8', newline='\n') as f:
    f.write(f'  {result}\n\n')
