#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 10-12-2013 16:49:07
#    Time-stamp: <17-12-2013 13:06:02>
#
#    File name : /home/mrmen/calcul-litteral.py
#    Description :
#

import random
import sympy

EXER = 5
QUESTION = 10
MONOME = 5

# preparation
variable = ["x", "y", "z", ""]
signe = ["+", "-"]
coeff = []
i=-9.5
while i<10:
    coeff.append(i)
    i+=1
i=-9
while i<10:
    coeff.append(i)
    i+=1

def texprint(poly):
    polynome = ""
    for monome in poly:
        tempCoeff = monome[0]
        tempVar = monome[1]
        if (len(monome)==3):
            tempSgn = monome[2]
        if (tempCoeff==0):
            polynome = polynome[:-2]
        elif (tempCoeff==1):
            if tempVar == "":
                polynome = polynome + "1"
            else:
                polynome = polynome + str(tempVar)
        else:
            if (tempVar == ""):
                polynome = polynome + str(tempCoeff)
            else:
                polynome = polynome + str(tempCoeff) + " MUL " + tempVar
        if len(monome)==3:
            polynome = polynome + tempSgn + " "
        else:
            polynome = polynome + " "
    return polynome

def solevandtexprint(poly):
    polynome = texprint(poly)
    polynome = polynome.replace("MUL", "*")
    x = sympy.var('x')
    y = sympy.var('y')
    z = sympy.var('z')
    result = str(sympy.simplify(polynome))
    return result.replace("*", " ")
    
# exercice
ListExer = []
for exer in range(EXER):
    ListExer.append([])
    for question in range(QUESTION):
        polynome = []
        for monome in range(MONOME):
            tempVar = variable[random.randint(0,len(variable)-1)]
            tempCoeff = coeff[random.randint(0,len(coeff)-1)]
            tempSgn = signe[random.randint(0,1)]
            if tempCoeff<0:
                tempCoeff = "(" + str(tempCoeff) + ")"
            L = []
            if (monome!=MONOME-1):
                L.append(tempCoeff)
                L.append(tempVar)
                L.append(tempSgn)
            else:
                L.append(tempCoeff)
                L.append(tempVar)
            polynome.append(L)
        ListExer[exer].append(polynome)


print("\\documentclass{article}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{enumerate}")
print("\\theoremstyle{definition}\\newtheorem{exercice}{Exercice}")
print("\\newtheorem{solution}{Solution}")
print("\\usepackage[margin=2cm]{geometry}")
print("\\usepackage{fancyhdr}")
print("\\fancyhf{}\\fancyhead[L]{Exercices de simplification}\\fancyhead[R]{Cinquieme}")
print("\\pagestyle{fancy}")
print("\\begin{document}")

for exer in range(EXER):
    print("\\begin{exercice}\n\n\\ \\bigskip\n\n")
    exo = ListExer[exer]
    count = 1
    print("\\begin{minipage}{0.5\\linewidth}")
    print("\\begin{enumerate}[a)]")
    for polynome in exo:
        print("\\item $"+texprint(polynome).replace("MUL"," ")+"$\n")
        if (count==5):
            print("\\end{enumerate}")
            print("\\end{minipage}")
            print("\\begin{minipage}{0.5\\linewidth}")
            print("\\begin{enumerate}[a)]")
            print("\\setcounter{enumi}{5}")
        count+=1
    print("\\end{enumerate}")
    print("\\end{minipage}")
    print("\\end{exercice}")
    print("\n\\vspace*{0.5cm}\n")

print("\n\n\\newpage\n\n")

for exer in range(EXER):
    print("\\begin{solution}\n\n\\ \\bigskip\n\n")
    exo = ListExer[exer]
    count = 1
    print("\\begin{minipage}{0.5\\linewidth}")
    print("\\begin{enumerate}[a)]")
    for polynome in exo:
        print("\\item $"+solevandtexprint(polynome)+"$\n")
        if (count==5):
            print("\\end{enumerate}")
            print("\\end{minipage}")
            print("\\begin{minipage}{0.5\\linewidth}")
            print("\\begin{enumerate}[a)]")
            print("\\setcounter{enumi}{5}")
        count+=1
    print("\\end{enumerate}")
    print("\\end{minipage}")
    print("\\end{solution}")
    print("\n\\vspace*{0.5cm}\n")



print("\\end{document}")
