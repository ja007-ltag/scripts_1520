data1 = """\
R_01G1SOV	1СП 2СП 4СП 3СП 5СП
R_01G2SOV	6СП 8СП 10СП 7СП
R_01G3SOV	12СП IНП ЧП IIНП\
"""
data2 = """\
R_01О1SOV	5СП 6СП 12СП
R_01О2SOV	2СП 8СП IНП
R_01О3SOV	4СП 10СП ЧП
R_01О4SOV	3СП 7СП IIНП
R_01О5SOV	1СП\
"""

res = {}
for line in data1.split('\n'):
    value, keys = line.split('\t')
    for key in keys.split():
        res[key] = [value]

for line in data2.split('\n'):
    value, keys = line.split('\t')
    for key in keys.split():
        res[key].append(value)

# print(len(res))
# print(res)

text = ''
for key in sorted(res.keys()):
    text += f'{key}:\n{res[key][0]}\n{res[key][1]}\n\n'

print(text)
