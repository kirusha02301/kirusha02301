d=str(input('vvedite primer'))
g=d.split()
a=float(g[0])
n=g[1]
b=float(g[2])
def plus(a,b):
    c=a+b
    return c
def minus(a,b):
    c=a-b
    return c
def multiplication(a,b):
    c=a*b
    return c
def division(a,b):
    c=a/b
    return c
def degree(a,b):
    c=a**b
    return c
if n=='+':
    print(plus(a,b))
if n=='-':
    print(minus(a,b))
if n=='*':
    print(multiplication(a,b))
if n=='/':
    print(division(a,b))
if n=='**':
    print(degree(a,b))