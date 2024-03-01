"""
Перевод русских символов в английские
"""

import transliterate

s = """25-29СГЕП	
19-23СГЕП	
1НАПГЕП		
1ПГЕП		
32-36СГЕП	
1АПГЕП		
 			

1ЧАПГЕП		
8-12СГЕП	
14-18СГЕП	

25-29АСГЕР	
19-23АСГЕР	
1НАПСГЕР	
32-36АСГЕР	
А1АПГЕР		
Б1АПГЕР		
 			

А1ПГЕР		
Б1ЧАПГЕР	
8-12АСГЕР	
14-18АСГЕР	

А1ЧАПГЕР	
Б1ПГЕР		
Б1НАПГЕР	
А1ЧАПГКР	
Б1ПГКР		
Б1НАПГКР	
"""
out = transliterate.translit(s, language_code='ru', reversed=True)

print(out)

def translit():
    dictionary = {}
    print(dictionary)
    pass