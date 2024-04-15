f=open('11111.txt')
kol=0
for i in f:
    b=i.split()
    perv=int(b[0])
    posl=int(b[3])
    c=[int(y) for y in b]
    c=sorted(c)
    if perv!=c[0] and perv!=c[3] and posl!=c[0] and posl!=c[3] and c[1]!=c[2]:
        if ((c[3]-c[0])%(c[2]-c[1]))==0:
            kol+=1
print(kol)

for n in range(4,100):
    s='3'+'7'*n
    while s.count('37')>0 or s.count('577')>0 or s.count('777')>0:
        if s.count('37')>0:
            s = s[:s.find('37')] +'7'+s[s.find('37')+2:]
        if s.count('577')>0:
            s = s[:s.find('577')] +'73'+s[s.find('577')+3:]
        if s.count('777')>0:
            s = s[:s.find('777')] +'5'+s[s.find('777')+3:]
    print(n,s)

pr=1
for x in range(12):
    for y in range(18):
        T=6*12**4 + 7*12**3 + x*12**2 +x*12 + 3 + 2*14**3 + x*14**2 + 9*14**1 + x + 4*15**4 +4*15**3 + x*15**2 + x*15 + 3 -(2*18**3 + x*18**2 + y*18 + 7)
        if T>0 and T%77==0:
            pr=pr*x*y
print(pr)


def prov(A):
    for x in range(1,1000):
        R = (((x%2==0)<= (x%13!=0)) or x+A>=1000)
        if R==False:return False
    return True

for A in range(1,1000):
    if prov(A):
        print(A)

def perevod(x,N):
    alf='0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    alf=sorted(alf)
    chis=''
    while x>0:
        chis=alf[x%N]+chis
        x=x//N
    return chis

f=open('11111.txt')
b = [int(y) for y in f]
c=[e for e in b if perevod(e,16)[-2:]=='0F']
maxs=max(c)
sums=0
kol=0
for x in range(len(b)-1):
    a1,a2=b[x],b[x+1]
    if (a1%7==0 or a2%7==0) and ((a1+a2)%7!=0) and (a1+a2)%maxs==0:
        kol+=1
        sums=max(sums,a1+a2)
print(kol,sums)

from ipaddress import*
net=ip_network('250.135.101.80/255.255.255.248')
kol=0
for i in net:
    k=bin(int(i))[2:]
    if k.count('0')%3==0:
        kol+=1
print(kol)

from ipaddress import*
net=ip_network('99.64.0.0/255.192.0.0')
kol=0
for i in net:
    k=bin(int(i))[-2:]
    if k=='11':kol+=1
print(kol)
