data = []
for s in open('27a(hard).txt'):
    x,y,v = [float(d) for d in s.split()]
    data.append([x,y,v])

def dist(p1,p2):
    x1,y1,v1 = p1
    x2,y2,v2 = p2
    return ((x1-x2)**2+(y1-y2)**2)**0.5

clusters = []
while data:
    cl = [data.pop()]
    for p in  cl:
        sosed = [p1 for p1 in data if dist(p,p1)<1]
        cl.extend(sosed)
        for p1 in sosed:data.remove(p1)
    clusters.append(cl)

print([len(cl) for cl in clusters])
 
from turtle import *
from random import *
tracer(0)
up()
for cl in clusters:
    color = random(), random(), random()
    for x,y,v in cl:
        goto(x*30, y*30)
        dot(3,color)
update()

def ves(cl):
    x,y,v = 0,0,0
    for p in cl:
        x1,y1,v1 = p
        if v1>v:
            x,y,v = p
    return [x,y,v]

socr = [ves(cl) for cl in clusters]
px = dist(socr[0],socr[1])
py = 0
for p in socr:
    x,y,v = p
    py += v
print(px*10000//1,py*10000//1)

