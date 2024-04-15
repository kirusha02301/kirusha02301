'''
#1
A = int(input())
B = int(input())
A = 2*(A//2)
a = [i for i in range(A+2,B,2)]
print(a)
'''
'''
#1.1
A = int(input())
for i in range(2,A):
    if A%i==0:
        print("Число не простое")
        break
else:
    print("Число простое")
'''
'''
#2
a = input().split()
x=0
for i in a:
    if 999<int(i)<10000:
        x+=1
print(x)
'''
'''
#3
a = input().split()
y = 0
for i in a:
    x = 0
    p = i
    while int(i) != 0:
        x = int(i) % 10 + x
        i = int(i)//10
    if x >y:
        y = x
        z = p
print(z)
'''
'''
#4
a = input().split()
for i in a:
    x = 0
    for j in range(1,int(i)+1):
        if int(i) % j == 0:
            x+=1
    if x ==5:
        print(i)
'''
'''
#4.4
A = input().split()
x = 0
for i in A:
    for j in range(2,int(i)):
        if int(i)%j==0:
            break
    else:
        x+=int(i)
print(x)
'''
'''
#5
A = input().split()
x = []
z = 1111111
for i in A:
    d = 0
    for j in range(2,int(i)):
        if int(i)%j==0:
            d+=1
    if d<z:
        z = d
for i in A:
    d = 0
    for j in range(2,int(i)):
        if int(i)%j==0:
            d+=1
    if d == z:
        x.append(i)
print(x)
'''
'''
#6
A = input().split()
e=1
for i in A:
    u = int(i)
    while int(i) !=0:
        z = int(i)%10
        i = int(i)//10
        if z%2==0:
            break
    else:
        e*=u
print(e)
'''
'''
#1
A = input().split()
x=0
y = 111111
z = 111111
for i in range(1,len(A)):
    if (int(A[i])%7==0 and int(A[i-1])%17!=0)  or (int(A[i-1])%7==0 and int(A[i])%17!=0) :
        x+=1
        y =  int(A[i]) + int(A[i-1])
    if y<z:
        z = y
if z ==111111:print("Таких пар нету")
else:print(x,z)
'''
'''
#2
A = input().split()
x=0
z = 111111
for i in range(1,len(A)):
    if (int(A[i])%3==0 and abs(int(A[i]))%10==6)  or (int(A[i-1])%3==0 and abs(int(A[i-1]))%10==6):
        x+=1
        if int(A[i]) < z:
            z = int(A[i])
        if  int(A[i-1]) < z:
            z = int(A[i-1])
print(x,z)
'''
'''
#3
A = input().split()
x=0
z = -111111
for i in range(1,len(A)):
    if (int(A[i])%9==0 and int(oct(abs(int(A[i-1])))[2:])%10==3 and int(A[i-1])%9!=0 )  or (int(A[i-1])%9==0 and int(oct(abs(int(A[i])))[2:])%10==3 and int(A[i])%9!=0):
        x+=1
        if int(A[i])>z:
            z = int(A[i])
        if int(A[i-1])>z:
            z = int(A[i-1])
print(x,z)
'''
'''
#4
A = input().split()
x = 0
z=111111
y = 111111
for i in range(1,len(A)):
    if int(A[i])>int(A[i-1]):
        x+=1
        z = abs(int(A[i])-int(A[i-1]))
    if z<y:
        y=z
print(x,y)
'''