clA = [[], []]
for s in open('27a(hard).txt'):
    x,y,v = [float(d) for d in s.split()]
    if y>15:
        clA[0].append([x,y,v])
    else:
        clA[1].append([x,y,v])

clB = [[], [], []]
for s in open('27b(hard).txt'):
    x,y,v = [float(d) for d in s.split()]
    if x<11:
        clB[0].append([x,y,v])
    elif x<19:
        clB[1].append([x,y,v])
    else:
        clB[2].append([x,y,v])
 
##print([len(cl) for cl in clA])
##from turtle import *
##from random import *
##tracer(0)
##up()
##screensize(10000,10000)
##for cl in clA:
##    color = random(), random(), random()
##    for x,y,v in cl:
##        goto(x*30, y*30)
##        dot(3,color)
##update()

def dist(p1,p2):
    x1,y1,v1 = p1
    x2,y2,v2 = p2
    return ((x1-x2)**2+(y1-y2)**2)**0.5

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

socr = [ves(cl) for cl in clA]
px = dist(socr[0],socr[1])
py = 0
for p in socr:
    x,y,v = p
    py += v
print(px*10000//1,py*10000//1)

ves_min = min([ves(cl)[2] for cl in clB])
buhti = [cl for cl in clB if ves(cl)[2]!=ves_min]
cen = [centr(cl) for cl in buhti]
q1 = dist(cen[0],cen[1])
q = [centr(cl) for cl in clB if ves(cl)[2]==ves_min]
q = [p for x in q for p in x]
q2 = q[0]+q[1]
print(q1*10000//1,q2*10000//1)


