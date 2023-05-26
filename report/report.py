"""
Для подсчёта часов в отчёте
"""

hours_05_23 = """
8
2
2
4
6
16
2
38
2
2
50
4
4
6
2
2
4
2
2
"""

def all_hours(s):
    return sum(int(i) for i in s.split())

print(all_hours(hours_05_23))
