abc = list('abwgdevzijklmnoprstufhcqx')
print(abc)

morze='.- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- - --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-'
m=morze.split()
print(m)
print(m[0])
input()
#перебор посимвольно текста for
#искали этот символ в алфавите по индексу и запоминали номер .index
#по этому номеру дергали элемент азбуки морзе [nomer]
text=input(введите слово...)
for i in text:
    num=abc.index(i)
    itog=itog+abcm[num]
print(itog)


