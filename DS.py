def prov(A):
    for x in range(1,100000):
        F = ((A+x<123)<=((x%5==0)<=(not(x%7==0))))
        if F==False:return False
    return True
for A in range(1,1000):
    if prov(A):
        print(A)
        break

f= open('17-378.txt')
b=[]
maxabs=-10000
kol=0
for i in f:
    b.append(int(i))
    if abs(int(i))%1001==0:
        maxabs=max(maxabs,abs(int(i)))
mins=11111111
for i in range(len(b)-1):
    a1,a2=b[i],b[i+1]
    if len(str(abs(a1)))==3 or len(str(abs(a2)))==3:
        if a1+a2>maxabs:
            kol+=1
            mins=min(mins,(a1+a2))
print(kol,mins)

# номера 6 7 10 11 12 16 18 22



def game(x,y,h):
    if (x<10 or y<10) and (h==4 or h==2):return True
    elif x>=10 and y>=10 and h<4:
        a = [game(x-3,y,h+1),game(x-1,y,h+1),game(x,y-1,h+1),game(x,y-3,h+1)]
        if h==0 or h==2:return all(a)
        if h==1 or h==3:return any(a)
    return False
for s in range(10,100):
    if game(13,s,0):
        print(s)

def f(x,stop):
    if x==stop:return True
    if x<stop:return False
    else:
        return f(x//2,stop) + f(x-2,stop)
print(f(28,10)*f(10,1))


f=open('24-111.txt').readline()

S =f.replace('A','1').replace('B','1').replace('X','1')
b = S.split('1')
maxs=0
for i in range(len(b)-6):
    if len(b[i]+b[i+1]+b[i+2]+b[i+3]+b[i+4]+b[i+5])>maxs:maxs=len(b[i]+b[i+1]+b[i+2]+b[i+3]+b[i+4]+b[i+5])
print(maxs+5)
