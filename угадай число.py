import fnmatch
def prost(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True

for i in range(0,10**9,2267):
    if fnmatch.fnmatch(str(i),'7*15?3*7'):
        b=[int(t) for t in str(i)]
        if prost(sum(b)):
            print(i,i/2267)

#24
f=open('24-197.txt').readline()
kol=0
maxs=0
for u in range(3):
    for x in range(u,len(f)-2,3):
        k=f[x]+f[x+1]+f[x+2]
        if k=='XXX' or k=='XYX' or k=='XZX' or k=='YXY' or k=='YZY' or k=='YYY':
            kol+=1
        else:
            maxs=max(kol,maxs)
            kol=0
print(maxs)

from turtle import*
tracer(0)
raz=50
screensize(10000,10000)
for i in range(7):
    goto(xcor()+6*raz,ycor()-9*raz)
    goto(xcor() - 6*raz, ycor() + 2*raz)
    goto(xcor() + 12*raz, ycor() + 3*raz)

up()
for x in range(-100,100):
    for y in range(-50,20):
        goto(x*raz,y*raz)
        dot(3,'blue')

update()
exitonclick()
