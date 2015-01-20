#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 12-03-2014 20:42:22
#    Time-stamp: <12-03-2014 21:08:02>
#
#    File name : /tmp/mult.py
#    Description :
#
import random

MULT = 30
MIN = 10
MAX = 1000

EXO = []

for i in range(MULT):
    ta = random.randint(MIN,MAX)
    tb = random.randint(MIN,MAX)
    a = max(ta,tb)
    b = min(ta,tb)
    EXO.append([a,b])

print("\\documentclass{article}")
print("\\usepackage{amsmath, xlop}")
print("\\usepackage[margin=2cm]{geometry}")
print("\\usepackage{multicol}")
print("\\usepackage{fancybox}")
print("\\newtheorem{exo}{Exercice}")
print("\\newtheorem{sol}{Solution}")
print("\\title{Exercices d'addition}")
print("\\date{}")
print("\\begin{document}")

print("\\maketitle")

print("\\begin{exo}\ \n\n\\bigskip\n\n")
print("\\begin{minipage}{0.5\linewidth}")
print("\\begin{enumerate}")

for j in range(MULT):
    if j!=0 and j%10==0:
        print("\\end{enumerate}")
        print("\\end{minipage}")
        print("\\end{exo}")
        print("")
        print("\\bigskip")
        print("")
        print("\\begin{exo}\ \n\n\\bigskip\n\n")
        print("\\begin{minipage}{0.5\linewidth}")
        print("\\begin{enumerate}")
    elif j!=0 and j%5==0:
        print("\\end{enumerate}")
        print("\\end{minipage}")
        print("\\begin{minipage}{0.5\linewidth}")
        print("\\begin{enumerate}")
        print("\\setcounter{enumi}{5}")
    print("\\item $"+str(EXO[j][0])+" + "+str(EXO[j][1])+"$")
    
print("\\end{enumerate}")
print("\\end{minipage}")
print("\\end{exo}")

print("\\newpage")

print("\\begin{multicols}{2}")
print("\\begin{sol}\ \n\n\\bigskip\n\n")
#print("\\begin{minipage}{0.5\linewidth}")
print("\\begin{enumerate}")

for j in range(MULT):
    if j!=0 and j%10==0:
        print("\\end{enumerate}")
#        print("\\end{minipage}")
        print("\\end{sol}")
        print("")
        print("\\bigskip")
        print("")
        print("\\begin{sol}\ \n\n\\bigskip\n\n")
#        print("\\begin{minipage}{0.5\linewidth}")
        print("\\begin{enumerate}")
    elif j!=0 and j%5==0:
        print("\\end{enumerate}")
#        print("\\end{minipage}")
#        print("\\begin{minipage}{0.5\linewidth}")
        print("\\begin{enumerate}")
        print("\\setcounter{enumi}{5}")
    print("\\item \shadowbox{\\opadd[lastcarry]{"+str(EXO[j][0])+"}{"+str(EXO[j][1])+"}}")
    
print("\\end{enumerate}")
#print("\\end{minipage}")
print("\\end{sol}")
print("\\end{multicols}")

print("\\end{document}")
