data = []
for s in open('27b(hard).txt'):
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
        sosed = [p1 for p1 in data if dist(p,p1)<1.4]
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

def centr(cl):
    m = []
    for p in  cl:
        s = sum(dist(p,p1) for p1 in cl)
        m += [[s,p]]
    return min(m)[1]

ves_min = min([ves(cl)[2] for cl in clusters])

buhti = [cl for cl in clusters if ves(cl)[2]!=ves_min]
cen = [centr(cl) for cl in buhti]
q1 = dist(cen[0],cen[1])
q = [centr(cl) for cl in clusters if ves(cl)[2]==ves_min]
q = [p for x in q for p in x]
q2 = q[0]+q[1]
print(q1*10000//1,q2*10000//1)

