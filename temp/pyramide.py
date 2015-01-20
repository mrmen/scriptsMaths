#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 11-02-2014 08:59:28
#    Time-stamp: <11-02-2014 16:36:29>
#
#    File name : /tmp/pyramide.py
#    Description :
#
import random
import sys
import hashlib
from sympy import *
from fractions import Fraction


if (len(sys.argv)>1):
    base = int(sys.argv[1])
else:
    base = 6

pyramide = []

pyramide.append([])
for i in range(base):
    num = random.randint(1,10)
#    try sys.argv[2]==0:
    denom = random.randint(1,10)
#    else:
#        denom = 1
    pyramide[0].append(Fraction(num,denom))
#    pyramide[0].append(random.randint(-5,5))

for j in range(base-1):
    pyramide.append([])
    levelDown = pyramide[j]
    for case in range(base-1-j):
        pyramide[j+1].append(levelDown[case]+levelDown[case+1])


sum = hashlib.md5()
sum.update(str(pyramide))


l = 1.5
print("\\documentclass{article}")
print("\\usepackage{tikz}")
print("\\usepackage{amsmath}")
print("\\begin{document}")

print("\\begin{center}\\underline{\\textbf{Exercice}}")
print("sum : "+sum.hexdigest())
print("\\end{center}")

print("\\bigskip")

print("\\begin{center}\\begin{tikzpicture}")

for elt in range(len(pyramide)):
    print("\\begin{scope}[shift={("+str(0.5*l*elt)+","+str(elt*l)+")}]")
    line = pyramide[elt]
    for i in range(len(line)):
        print("\\draw ("+str(i*l)+",-"+str(0.5*l)+") -- ("+str((i+1)*l)+",-"+str(0.5*l)+") -- ("+str((i+1)*l)+","+str(0.5*l)+") -- ("+str(i*l)+","+str(0.5*l)+") -- cycle ;")
        string = str(line[i])
        if string.find("/")!=-1:
            string = string.replace("/","}{")
            string = "$\\dfrac{"+string+"}$"
        if (elt<=1):
            if 1-(i%2):
                print("\\draw ("+str((i+0.5)*l)+",0) node{"+string+"};")
    print("\\end{scope}")

print("\\end{tikzpicture}\\end{center}")



print("\\newpage")

print("\\begin{center}\\underline{\\textbf{Solution}}")
print("sum : "+sum.hexdigest())
print("\\end{center}")

print("\\begin{center}\\begin{tikzpicture}")

for elt in range(len(pyramide)):
    print("\\begin{scope}[shift={("+str(0.5*l*elt)+","+str(elt*l)+")}]")
    line = pyramide[elt]
    for i in range(len(line)):
        print("\\draw ("+str(i*l)+",-"+str(0.5*l)+") -- ("+str((i+1)*l)+",-"+str(0.5*l)+") -- ("+str((i+1)*l)+","+str(0.5*l)+") -- ("+str(i*l)+","+str(0.5*l)+") -- cycle ;")
        string = str(line[i])
        if string.find("/")!=-1:
            string = string.replace("/","}{")
            string = "$\\dfrac{"+string+"}$"
        print("\\draw ("+str((i+0.5)*l)+",0) node{"+string+"};")
    print("\\end{scope}")

print("\\end{tikzpicture}\\end{center}")
print("\\end{document}")
