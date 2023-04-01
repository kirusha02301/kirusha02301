a=[int(x) for x in input().split()]
e=len(a)
Fl=False
while not(Fl):
    for i in range(e):
        f=a[i]
        for x in range(i,e):
            if f<=a[x]:
                continue
            else:
                a[i],a[x]=a[x],a[i]
        
    print(a)
    if all(a[i]<=a[i+1] for i in range(e-1)):
        Fl=True
print('end - ',a)
