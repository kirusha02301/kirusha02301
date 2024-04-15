'''
#(№ 6676) (ЕГЭ-2023) Текстовый файл 24-264.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита и цифры.
# Определите максимальную длину подстроки, которая может являться записью числа в шестнадцатеричной системе счисления.
S = open('6676.txt').readline()
for x in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    if x not in 'ABCDEF':
        S = S.replace(x,' ')
S = S.split()
res = max(S,key = len)
print(res,len(res))
'''


'''
#(№ 6675) (ЕГЭ-2023) Текстовый файл 24-263.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита.
# Определите максимальную длину подстроки, в которой символ Y встречается не более 150 раз.
S = open('6675.txt').readline()
S = S.split('Y')
max = 0
for i in range(len(S)-151):
    srez='Y'.join(S[i:i+151])
    if len(srez)>max:
        max = len(srez)
print(max)
'''


'''
#(4526)Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 106 символов.
# Определите максимальное количество идущих подряд символов, среди которых не более трёх точек.
S = open('4526.txt').readline()
S = S.split('.')
max = 0
res = 0
for i in range(len(S)-4):
    srez = '.'.join(S[i:i+4])
    if len(srez)>max:
        max = len(srez)
        res = srez
print(max,res)
'''


'''
#(№ 6678) (В. Шубинкин) Текстовый файл 24-268.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита и цифры.
#В файле записаны числа в девятнадцатеричной системе счисления, окружённые символами, не являющимися цифрами в этой системе счисления или началом/концом файла.
#Лидирующие нули в записи чисел не допускаются.
#Определите самое большое чётное число в этом файле.
# Например, в последовательности символов FF2FTZBBC8R420Y0CCCE содержится 3 числа в девятнадцатеричной системе счисления: FF2F, BBC8 и 420.
# Самое большое чётное число – BBC8. Число CCCE не учитывается, так как перед ним стоит ноль.
#Алфавит двадцатеричной системы счисления: 0123456789ABCDEFGHI.
S = open('6678.txt').readline()
for x in 'QWRTYUOPSJKLZXVNM':
     S = S.replace(x,' ')
S = S.split()
k=0
d = []
for j in S:
    if j[0]=='0':
        S[k]=" "
    else:
        d.append(j)
    k+=1
max1 = 0
for h in range(len(d)):
    if int(d[h],19) > max1 and int(d[h],19)%2==0:
        max1 = int(d[h],19)
        max = d[h]
print(max)
'''




'''
#(№ 5390) (А. Калинин) Текстовый файл 24-215.txt содержит строку из символов A, B, C и цифр 1, 2, 3, всего не более чем 106 символов.
# Определите максимальное количество идущих подряд троек символов вида «цифра + цифра + буква».
S = open('5390.txt').readline()
ts = ''
ms = ''
for j in range(3):
    for i in range(j,len(S)-2,3):
        if S[i] in '123' and S[i+1] in '123' and S[i+2] in 'ABC':
            ts+= S[i]+S[i+1]+S[i+2]
            if len(ts)>len(ms): ms = ts
        else: ts=""
print(len(ms)//3)
'''



'''
#(№ 5230) Текстовый файл 24-1.txt содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите максимальное количество идущих подряд символов, среди которых гласные буквы (A, E, I, O, U и Y) в общей сложности встречаются не более пяти раз.
S = open('5230.txt').readline()
for i in 'AEIOUY':
    S = S.replace(i,' ')
S = S.split(' ')
max = 0
str = 0
for j in range(len(S)-6):
    srez = '1'.join(S[j:j+6])
    if len(srez) > max:
        max = len(srez)
        str = srez
print(max,str)
'''


'''
#(№ 5041) Текстовый файл 24-197.txt содержит строку из заглавных латинских букв X, Y и Z, всего не более чем из 106 символов. 
#Определите максимальное количество идущих подряд троек символов X*Y или Z*Y, где * обозначает один любой символ.
S = open('5041.txt').readline()
ts = ''
ms = ''
for j in range(3):
    for i in range(j,len(S)-2,3):
        if S[i] in 'XZ'  and S[i+2] in 'Y':
            ts+= S[i]+S[i+1]+S[i+2]
            if len(ts)>len(ms): ms = ts
        else: ts=""
print(len(ms)//3)
'''


'''
#(№ 5042) Текстовый файл 24-197.txt содержит строку из заглавных латинских букв X, Y и Z, всего не более чем из 106 символов. 
# Определите максимальное количество идущих подряд троек символов X*X или Y*Y, где * обозначает один любой символ.
S = open('5042.txt').readline()
ts = ''
ms = ''
for j in range(3):
    for i in range(j,len(S)-2,3):
        if (S[i] in 'X'  and S[i+2] in 'X') or (S[i] in 'Y'  and S[i+2] in 'Y'):
            ts+= S[i]+S[i+1]+S[i+2]
            if len(ts)>len(ms): ms = ts
        else: ts=""
print(len(ms)//3)
'''

'''
#	(№ 4753) Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 106 символов. 
#	Определите максимальное количество идущих подряд символов, среди которых нет гласных букв (символов A, E, I, O, U, Y), но есть не менее 6 точек.
S = open('4753.txt').readline()
for x in 'AEIOUY':
    S = S.replace(x,' ')
m = S.split()

m1 = [x for x in m if x.count('.')>=6]
res = max(m1,key = len)
print(res,len(res))
'''

'''
#функция перевода систем счисления
def per(x,N):
    res = ''
    alf = '0123456789ABCDEFGHI'
    while x>0:
        res = alf[x%N] + res
        x//=N
    return res
print(per(число в десятичной,в какой системе надо получить число))
'''