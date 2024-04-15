'''
#8
from functools import reduce
a = [13,123,134132,2133,47]
def prost(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
b = [i for i in a if prost(i)==True]
print(reduce(lambda x,y:x+y,b))
print(reduce(lambda x,y:x*y,b))
'''


'''
#9
a = [1,13,123,134132,2133,2222,2112,2212,111,2222222]
x = 0
while x!=len(a):
    k = 0
    for i in str(a[x]):
        if i in '24680':
            k+=1
    if k >2:
        a.pop(x)
    else:
        x+=1
print(a)
'''


'''
#10
a = [1,13,123,134132,2133,2222,2112,2212,111,123321]
b=[]
for i in a:
    k=0
    if i%2==0 and len(str(i))%2==0:
        for j in range(len(str(i))//2):
            if str(i)[j]==str(i)[-(j+1)]:
                k+=1
        if k*2==len(str(i)):
            b.append(i)
print(b)
'''

'''
#2666
n = [] #все числа не кратные 6
kr6 = [] #все числа кратные 6
kr2 = [] #все числа кратные 2 но не кратные 3
kr3 = [] #все числа кратные 3 но не кратные 2
f = open('2666A.txt')
N = f.readline()
for line in f:
    x = int(line)
    if x%6==0: kr6.append(x)
    elif x%2==0: kr2.append(x)
    elif x%3==0: kr3.append(x)
    else: n.append(x)

kr6.sort()
print(max(kr6[-2]*kr6[-1],max(kr2)*max(kr3),max(kr6)*max(n)))
'''

'''
#2672
n = [] #все числа не кратные 6
kr6 = [] #все числа кратные 6
kr2 = [] #все числа кратные 2 но не кратные 3
kr3 = [] #все числа кратные 3 но не кратные 2
f = open('2672B.txt')
N = f.readline()
for line in f:
    x = int(line)
    if x % 6 == 0:
        kr6.append(x)
    elif x % 2 == 0:
        kr2.append(x)
    elif x % 3 == 0:
        kr3.append(x)
    else:
        n.append(x)
kol=len(kr6)*(len(kr2)+len(kr3)+len(n))+len(kr2)*len(kr3)+(len(kr6)*(len(kr6)-1))//2
print(kol)
'''

'''
#2674
f = open('2674A.txt')
N = f.readline()
ost = [0 for i in range(12)]
for line in f:
    num = int(line)
    ost[int(line)%12]+=1
s=ost[0]*(ost[0]-1)//2+ost[6]*(ost[6]-1)//2
for i in range(1,6):
    s+=ost[i]*ost[12-i]
print(s)
'''

'''
#2676
k=0
f = open('2676B.txt')
N = f.readline()
kr13 = []
b = []
for line in f:
    if int(line)%13==0:kr13.append(int(line))
    else:b.append(int(line))
for i in range(len(kr13)):
    for j in range(len(b)):
        if (kr13[i]+b[j])%2==1:
            k+=1

for m in range(len(kr13)-1):
    for l in range(m+1,len(kr13)):
        if (kr13[m]+kr13[l])%2==1:
            k+=1
print(k)
'''

'''
#2676
f = open('2676B.txt')
N = f.readline()
kr13c =[]
kr13nc =[]
nkr13c =[]
nkr13nc =[]
for line in f:
    x = int(line)
    if x%13==0:
        if x%2==0: kr13c.append(x)
        else: kr13nc.append(x)
    else:
        if x%2==0: nkr13c.append(x)
        else: nkr13nc.append(x)
s=len(kr13c)*len(kr13nc)+len(nkr13c)*len(kr13nc)+len(kr13c)*len(nkr13nc)
print(s)
'''

'''
#2920
def koldel(x):
    b = []
    for i in range(1,x+1):
        if x%i==0:
            b.append(i)
    return b
for i in range(100812,100923+1):
    if len(koldel(i))==6:
        print(i,koldel(i)[-2],i)
'''

'''
def count_divs(N):
    m = set()
    for x in range(1,int(x**0.5)+1):
        if N%x==0:
            m.add(x)
            m.add(N//x)
    return m
'''











'''
#2579
def kol_del(x):
    b = []
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            b.append(i)
            b.append(x//i)
    return b
maks = 0
k=0
for i in range(286_564,287_270):
    c = sorted(kol_del(i))
    x = len(c)
    if x>=k:
        k=x
        delit = c[-2]
print(k,delit)
'''

'''
#2615
def count_divs(N):
    m = set()
    for x in range(2,int(N**0.5)+1):
        if N%x==0:
            m.add(x)
            m.add(N//x)
    return m


b = [int(i) for i in range(int(525_784_203**0.5),int(728_943_762**0.5)+1)]
for j in b:
    g = j**2
    if len(count_divs(g)) == 3:
        print(int(j)**2,max(count_divs(g)))
'''
