not_find = [
    'Controller:',
    'Address:',
    'Type:',
    'Converter:',
    'Orders',
    'Statuses',
    '.' * 52,
    '\t' * 6
]

res = []
for line in open('OCData'):
    if not line.strip(): continue

    for target in not_find:
        if line.find(target) != -1:
            break
    else:
        line = line.strip().split('\t')[1]
        if line not in res:
            res.append(line)

if __name__ == '__main__':
    print(res)
    print(len(res))
