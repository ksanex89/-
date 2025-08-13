data = []
for s in open('27(med)b.txt'):
    x,y = [float(d) for d in s.split()]
    data.append([x,y])
 
from math import dist
 
clusters = []
while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p,p1)<1]
        cl.extend(sosed)
        for p1 in sosed: data.remove(p1)
    clusters.append(cl)
 
print([len(cl) for cl in clusters])
 
from turtle import *
from random import *
tracer(0)
up()
for cl in clusters:
    color = random(), random(), random()
    for x,y in cl:
        goto(x*30, y*30)
        dot(3,color)
update()


def need(cl):
    d = len(cl)
    g = 0
    for p in cl:
        x,y = p
        if ((x+y)//1)%2 == 0: g+=1
    if d-g<g: return 1

def centr(cl):
    sx = sum(x for x,y in cl)/len(cl)
    sy = sum(y for x,y in cl)/len(cl)
    return [sx,sy]

gryadka = [cl for cl in clusters if need(cl)]
pugalo = [centr(cl) for cl in gryadka]

px = sum(x for x,y in pugalo)
py = sum(y for x,y in pugalo)

print(px*10000//1,py*10000//1)

