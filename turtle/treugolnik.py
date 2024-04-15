print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=(((x or y)==(y<=z)) or w)
                if f==0:
                    print(x,y,z,w)



from turtle import *
tracer(0)
delay(0)
screensize(1000,1000)
M=50
lt(90)
for i in range(4):
    fd(3*M)
    left(270)
    fd(5*M)
    rt(90)
lt(270)
for i in range(3):
    fd(5*M)
    rt(90)
    fd(3*M)
    lt(270)
up()
for x in range(-9,9):
    for y in range(-9,9):
        goto(x*M,y*M)
        dot(3,'Blue')
update()
exitonclick()

from itertools import *
kol=0
for i in product('ПРИКАЗ',repeat=4):
    x=''.join(i)
    if x.count('К')==1:
        kol+=1
print(kol)

def game(x,h):
    if x==0 and h==2:return True
    elif x>0 and h<2:
        a = [game(x-5,h+1),game(x//3,h+1)]
        if h==0: return all(a)
        if h==1: return any(a)
    return False

for S in range(100,1,-1):
    if game(S,0):
        print('1-',S)
        break

def game(x,h):
    if x==0 and h==3:return True
    elif x>0 and h<3:
        if x>=5:a = [game(x-5,h+1),game(x//3,h+1)]
        else:a = [game(x//3,h+1)]
        if h==0: return any(a)
        if h==1: return all(a)
        if h==2: return any(a)
    return False
v=[]
for S in range(100,1,-1):
    if game(S,0):
        v.append(S)
print('2-',min(v),max(v))


def game(x,h):
    if x==0 and (h==4 or h==2):return True
    elif x>0 and h<4:
        if x>=5:a = [game(x-5,h+1),game(x//3,h+1)]
        else:a = [game(x//3,h+1)]
        if h==0: return all(a)
        if h==1: return any(a)
        if h==2: return all(a)
        if h == 3: return any(a)
    return False
for S in range(100,1,-1):
    if game(S,0):
        print('3-',S)
        break
