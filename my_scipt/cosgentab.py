data = '''
.	PREDEF_ON	274		NONE		HIGH		NO		NO
.	ALL_AU_OFF	275		NONE		HIGH		NO		NO
'''

data = data.strip()

for line in data.split('\n'):
    line = line.strip()

    if not line:
        print()
        continue

    if line[0] == '.':
        s0 = line[0]
        line = line[1:]
    else:
        s0 = ' '

    # s0, line = line[:1], line[1:]
    s1,s2,s3,s4,s5,s6 = line.split()
    p1 = len('COS1_COM_NOT_OK')
    p2 = len('Eventcode  ')
    p3 = len('Pretest    ')
    p4 = len('Priority   ')
    p5 = len('Pretest ind.   ')
    p6 = len('Vital comm  ')
    print(f"{s0}   {s1:{p1}} {s2:{p2}} {s3:{p3}} {s4:{p4}} {s5:{p5}} {s6:{p6}}")
