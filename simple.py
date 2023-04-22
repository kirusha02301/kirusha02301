import PySimpleGUI as sg
import webbrowser
sg.theme('LightBlue2')
urls = {
    'Google':'https://www.google.com',
    'Amazon':'https://www.amazon.com/',
    'NASA'  :'https://www.nasa.gov/',
    'Python':'https://www.python.org/',
        }  # Set the theme
s=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19, 20, 21','22','23','24','25','26','27b']
a=[
'''
1) определить точки, из которых выходят 3 линии
2) поподставять эти точки и , определить длины линий между ними и увидеть точки соединённые двумя дорогами.
3) поподставять и потом посчитать ответ
''',
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(y<=x) or (z<=w) or not(z))==False:
                    print(x,y,z,w)''',
'''
1) используем фильтр (раздел данных)
2) далее используем мозг и считаем ответ (иногда нужно скопировать таблицу по значениям и использовать функции)
'''
,'''
1) расписать 2-ичное древо
2) внести известные данные
3) Соотнести количество вариантов с количеством символов, начиная с минимального кода. 
''',
'''
a=bin(79)[2:]
for i in range(2):
    a=a+str((a.count('1')%2))
print(a)
''',
'''
1) Вспомнить команды черепахи
2) оранизовать алгортм задачи
3) рисуем точки из начала координат с помощью goto()
4) считаем точки
from turtle import *
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(2)
done()
''',
'''
1) Испольуем формулу V=M*i*t для звука
t - время
i - раширение
m - частота дискретезации
v - объем файла в битах
''',
'''
count=0
for a in range (1,8):
    for b in range (8):
        for c in range (8):
            for d in range (8):
                for e in range (8):
                    s=str(a)+str(b)+str(c)+str(d)+str(e)
                    if s.count('6')==1:
                        if s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0:
                            count+=1
                        if s.index('6')==0 and int(s[1])%2==0:
                            count+=1
                        if s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
                            count+=1
print(count)
''',
'''
tt=\'''66;39;77;31;132;117\'''
tt=t.split(';')
n=list(map(int,tt))
c=0
for i in range (6400):
    b=i*6
    f=n[b]
    s=n[b+1]
    trd=n[b+2]
    fo=n[b+3]
    fiv=n[b+4]
    six=n[b+5]
    Y=[f,s,trd,fo,fiv,six]
    d=0
    T=False
    diff=0
    sums=0
    for a in range(6): 
       d+=Y.count(Y[a]) 
       if d==8 and a==5:
         T=True
    for p in range(6):
      if Y.count(Y[p])==2:
         sums=2*Y[p]
      if Y.count(Y[p])==1:
         diff+=Y[p]
    diff==diff/4
    if sums>=(diff/4) and diff!=0 and sums!=0 and T:
      c+=1
print(c)''',
'''
1) открыть файл, нажать "Ctrl + f"
2) выбрать параметры поиска: "учитывать регист" и "Только слово целиком"
''','''11   
''',
'''
nums=[2,3,5,7]
for i in range(8,1000):
    flag=True
    for b in range(len(nums)):
        if i%nums[b] == 0:
            flag=False
    if flag:
        nums.append(i)
print(nums)
for n in range(30):
    for i in range(len(nums)):
        if 4*n + 117 ==nums[i]:
            print(n)''','''
1) старт маркеруется 1
2) анализируем пункты, в которые можно попасть по 1 дороге
3) позже большие, но строго следовать маршруту''',
'''
al='0123456789abcde'
for i in al:
    s=int(f'123{i}5',15) + int(f'1{i}233',15)
    if s%14==0:
        print(int(str(s//14),10))
''','''
for a in range(0,100):
    if all(((x%3==0) <= (x%5!=0)) or ((x+a)>=70) for x in range(1,10000)):
        print(a)
''',
'''it1=1
it2=1
for x1 in range(1,2024):
    it1=it1*x1
for x2 in range(1,2021):
    it2=it2*x2
print(it1/it2)
''',
'''
with open('17.txt')as f:
    a=[int(x)for x in f]
    g=[x for x in a if x%10==3]
    g=max(g)
    cs=[]
    for x,y in zip(a,a[1:]):
        if (((abs(x)%10==3) and (abs(y)%10!=3)) or ((abs(y)%10==3) and (abs(x)%10!=3))) and (x**2+y**2>=g**2):
            cs.append(x**2+y**2)
    print(len(cs),max(cs))
            
''','''
1) левый верхний угол берём значение из 1 таблицы
2) в ячейке справа складываем значение этой ячейки из таблицы 1 и значения 1 ячейки, аналогично для ячейки снизу
3) далее используем макс()+зн этой ячейки из таблицы 1 (макс() для ячеек сверху с снизу относительно даной)
4) за барьерами используем формулы сложения верхнего и данного значения , аналогично для горизонтального.
''','''
1) нарисовать двоичное дерево, начиная с победных ходов
2) расписываем дерево на 4 и более хода
3) считаем по усл задачи где чей ход extra (обычно ответ это число, которое можно получить только 1 способом)''','''
1) каждому процессу присваиваем цвет
2) закрашиваем клеточки в таблице относительно конца процесса
'''
,'''
def f(x,y):
    if x>y or x==17:
         return 0
    elif x==y:
         return 1
    return(f(x+1,y))+f(x*2,y)
print(f(1,10)*f(10,35))
    
''','''
with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('F','S').replace('D','S').replace('A','G').replace('O','G')
    s=s.replace("SG",'*')
    k=0
    kmax=0
    for i in s:
        if i=='*':
            k+=1
            kmax=max(k,kmax)
        else:
            k=0
    print(kmax)
''','''
for i in range(2023,10**10,2023):
    num=str(i)
    if (num[0]=='1') and (num[2:6]=='2139') and (num[-1]=='4'):
        print(i,i//2023)''',
'''
with open('26.txt') as f:
    s=[int(x) for x in f]
    s=sorted(s[1:],reverse=True)
    k,mini=1,s[0]
    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
    print(k,mini)
''',
'''with open('27-B.txt') as f:
    a=[int(x) for x in f]
    l=len(a)
    d=a+a
    allcost=[]
    res=0
    for i in range(l,(l//2)):
        cost=0
        v=d[i:i+l]
        for x in range(v):
            cost+=v[x]*x
        allcost.append(cost)
     mi=min(allcost)
            
'''

]
# Define the layout
layout = [[sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(90,50), key='outputt')],
          [sg.Button('Process Input', font=('Arial', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('urls', font=('Arial', 12), button_color=('white', '#4CAF50'), key='button')]]

# Create the window
window = sg.Window('ЕГЭ архив by Silkov Alexandr', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        choice=a[s.index(values['Combo'])]
        window['outputt'].update(choice)
    if event == 'button':
       urls = {
    'Google':'https://www.google.com',
    'Amazon':'https://www.amazon.com/',
    'NASA'  :'https://www.nasa.gov/',
    'Python':'https://www.python.org/',
}

    items = sorted(urls.keys())

    sg.theme("DarkBlue")
    font = ('Courier New', 16, 'underline')

    layout = [[sg.Text(txt, tooltip=urls[txt], enable_events=True, font=font,
    key=f'URL {urls[txt]}')] for txt in items]
    window = sg.Window('Hyperlink', layout, size=(250, 150), finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event.startswith("URL "):
            url = event.split(' ')[1]
            webbrowser.open(url)
        print(event, values)
# Close the window
window.close()
