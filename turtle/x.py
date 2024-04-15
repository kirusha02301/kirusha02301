from turtle import *
tracer(0)
delay(0)
left(90)
M=30
screensize(8000,8000)
for i in range(2):
    fd(10*M)
    right(90)
    fd(18* M)
    right(90)
up()
fd(5*M)
rt(90)
fd(7*M)
left(90)
down()
for i in range(2):
    fd(10*M)
    right(90)
    fd(7 * M)
    right(90)

up()
for x in range(-50,100):
    for y in range(-50,100):
        goto(x*M,y*M)
        dot(3,'green')
exitonclick()
update()

#26
f=open('26-123.txt')
#f=open('test.txt')
M,N=map(int,f.readline().split())#M-кол парковок N-кол заявок
kolsam=0
parkovki=[[0,1]]*M
b=[]
for i in f:
    vrem,prod,nomers,nomerk=map(int,i.split())
    b.append([vrem,vrem+prod,nomers-1,nomerk-1])
b.sort(key=lambda x:x[1])
obshee = 0
def sumpar(parkovki):
    sums=0
    for y in parkovki:
        sums+=y[0]
    return sums
for i in range(1,2000):
    for j in range(len(parkovki)):
        parkovki[j][1]=1
    for a in b:
        k1,k2,l1,l2=a[0],a[1],a[2],a[3]
        if i==k1:
            if parkovki[l1][0]==0 and parkovki[l1][1]==1:
                obshee+=1
            elif parkovki[l1][0]>0:
                parkovki[l1][0]-=1
        elif i==k2:
            parkovki[l2][0]+=1
            parkovki[l2][1]=0
    kolsam=max(obshee-sumpar(parkovki),kolsam)
print(obshee,kolsam)
