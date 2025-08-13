clA = [[], []]

for s in open('27(med)a.txt'):
    x,y = [float(d) for d in s.split()]
    if x>5:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

clB = [[], [], []]

for s in open('27(med)b.txt'):
    x,y = [float(d) for d in s.split()]
    if y<12:
        clB[0].append([x,y])
    elif y<21:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])
 
##print([len(cl) for cl in clB])
##from turtle import *
##from random import *
##tracer(0)
##up()
##screensize(10000,10000)
##for cl in clB:
##    color = random(), random(), random()
##    for x,y in cl:
##        goto(x*30, y*30)
##        dot(3,color)
##update()

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

gryadkaA = [cl for cl in clA if need(cl)]
pugaloA = [centr(cl) for cl in gryadkaA]
px = sum(x for x,y in pugaloA)
py = sum(y for x,y in pugaloA)
print(px*10000//1,py*10000//1)

gryadkaB = [cl for cl in clB if need(cl)]
pugaloB = [centr(cl) for cl in gryadkaB]
px = sum(x for x,y in pugaloB)
py = sum(y for x,y in pugaloB)
print(px*10000//1,py*10000//1)

