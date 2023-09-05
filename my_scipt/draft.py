s = 'hello'
t = [1, 2, 3]

loc_var = [i for i in dir() if not i.startswith('_')]

for var in loc_var:
    if var != 'os':
        print(f'{var} = {locals()[var]}')
        # print(f'{var} = {os.getenv(var)}')
