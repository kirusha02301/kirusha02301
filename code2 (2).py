#27 Шастин
# f=open('1777.txt')
#f=open('27A (1).txt')
from functools import cache
import sys
f = open('27B.txt')
N, W, K = map(int, f.readline().split())  # W-вмещаемость сейфа,N-кол всего слитков,K-макс вес серебра
vestype1 = []
vestype2 = []
for i in f:
    a1, a2 = map(int, i.split())
    if a2 == 0:
        vestype1.append(a1)
    if a2 == 1:
        vestype2.append(a1)
vestype1.sort()  # серебро
vestype2.sort()

spis1 = [[e, 0] for e in range(0, K + 1)]
sys.setrecursionlimit(3000)
@cache
def g1(k, tek, i, stopi):
    if tek > k:
        return 0
    elif tek == k:
        return 1
    elif i >= stopi:
        return 0
    else:
        return g1(k, tek, i + 1, stopi) + g1(k, tek + vestype1[i], i + 1, stopi)
for y in range(0, len(spis1)):
    spis1[y][1] = g1(spis1[y][0], 0, 0, len(vestype1))
print(spis1)

spis2 = [[e, 0] for e in range(W,W-K-1,-1)]
sys.setrecursionlimit(3000)
@cache
def g2(k, tek, i, stopi):
    if tek > k:
        return 0
    elif tek == k:
        return 1
    elif i >= stopi:
        return 0
    else:
        return g2(k, tek, i + 1, stopi) + g2(k, tek + vestype2[i], i + 1, stopi)


for y in range(0, len(spis2)):
    spis2[y][1] = g2(spis2[y][0], 0, 0, len(vestype2))
print(spis2)
kol = 0
for t in range(len(spis1)):
    r = spis1[t][1] * spis2[t][1]
    kol += r
print(kol)
is2 = [[e, 0] for e in range(W, W - K - 1, -1)]
