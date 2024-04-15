'''
def n1():
    print('Привет мир!')
def n2():
    for i in range (1,11):
        print(i)
def n3(x):
    print(x*x)
def n4(x):
    for i in range(1,x+1):
        if x % i==0:
            print(i)
def n5(x):
    y=1
    for i in range(1,x+1):
        y*=i
    print(y)
def n6(x:int):
    for i in range(1,x):
        if x % i ==0:
            y =i
    return(y)
def n7(x,y):
    for i in range(2,min(x,y)+1):
        if x % i ==0 and y % i ==0:
            return(i)
    return('Общих делителей нет')

#Первая часть
#1
def nomer1(x):
    return x/1000
#print(nomer1(int(input())),'кг')

#2
def nomer2(x):
    return x//10+x%10
#print(nomer2(int(input())))

#3
def nomer3(x,y,z):
    for i in range(min(x,y,z)+1,2,-1):
        if x%i==0 and y%i==0 and z%i==0:
            return(i)
    return('Общих делителей нету')
#print(nomer3(40,21,80))

#4
def nomer4(x,y,z):
    for i in range(max(x,y,z),x*y*z):
        if i % x ==0 and i % y ==0 and i % z ==0:
            return(i)
    return(x*y*z)
#print(nomer4(2,45,135))

#5
def nomer5(a):
    y=0
    for i in a:
        if int(i)%2==0:
            y+=int(i)
    return(y)
#print(nomer5(input().split()))

#6
def nomer6(x):
    if x<100 or x>999: return('Число не трехзначное')
    y=x//100+x%100//10+x%10
    return(y)
#print(nomer6(int(input())))

#7
def nomer7(x,y):
    z=int(str(x)[:1])*int(str(y)[:1])
    return(z)
#print(nomer7(212223,3))

#8
def nomer8(s):
    k = "аяуюоеэиы"
    b=0
    for i in s:
        if i in k:
            b+=1
    return(b)
#print(nomer8(input()))

#9
def nomer9(s):
    k = 1
    for i in s:
        if i == " ":
            k+=1
    return(k)
#print(nomer9(input()))
'''


'''
#Вторая часть
#1
def stepen(chislo,stpn):
    if stpn==0:
        return 1
    if stpn>0:
        return chislo*stepen(chislo,stpn-1)
    if chislo==0:
        return 'ошибка'
    if stpn<0:
        return 1/chislo*stepen(chislo,stpn+1)
print(stepen(2.5,-1))

#2
'''

















