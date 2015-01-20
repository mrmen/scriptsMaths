#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 06-02-2014 16:29:05
#    Time-stamp: <06-02-2014 17:29:29>
#
#    File name : /tmp/factor.py
#    Description :
#
import sympy
import random

EX = 5
QUES = 10

MIN=1
MAX=120

def getCalc():
    facteur = []
    facteur.append(random.randint(MIN,MAX))
    a = random.randint(MIN,MAX)
    if (sympy.gcd(a,facteur[0])) == 1:
        facteur.append(a+1)
    else:
        facteur.append(a)
    return facteur

def getSol(nb1, nb2):
    gcd = sympy.gcd(nb1,nb2)
    if (gcd==1):
        print("Il n'existe pas de facteurs commun pour "+str(nb1)+" et "+str(nb2)+"(ils sont premiers entre eux).")
        print("On ne peut donc pas factoriser cette expression.")
    else:
        divnb1 = int(nb1/gcd)
        divnb2 = int(nb2/gcd)
        print("\\begin{align*}")
        print(str(nb1)+"x + "+str(nb2)+"y")
        print("& = {\\color{red}"+str(gcd)+"}\\times "+"{\\color{blue}"+str(divnb1)+"}"+"\\times x + {\\color{red}"+str(gcd)+"}\\times "+"{\\color{DarkGreen}"+str(divnb2)+"}"+"\\times y\\\\")
        print(" & = {\\color{red}"+str(gcd)+"}("+"{\\color{blue}"+str(divnb1)+"} x + "+"{\\color{DarkGreen}"+str(divnb2)+"}y"+")")
        print("\\end{align*}")

def printSolution(List):
    for exer in List:
        print("\\begin{solution}\\ ")
        print("")
        print("\\bigskip")
        i = 1
        print("\\begin{minipage}{0.5\\linewidth}")
        print("\\begin{enumerate}")
        for ques in exer:
            if (i==6):
                print("\\end{enumerate}")
                print("\\end{minipage}")
                print("\\begin{minipage}{0.5\\linewidth}")
                print("\\begin{enumerate}\\setcounter{enumi}{5}")
            facteur1 = ques[0]
            facteur2 = ques[1]
            print("\\item")
            getSol(facteur1,facteur2)
            i+=1
        print("\\end{enumerate}")
        print("\\end{minipage}")
        print("\\end{solution}")

def printEnonce(List):
    for exer in List:
        print("\\begin{exo}\\ ")
        print("")
        print("\\bigskip")
        i = 1
        print("\\begin{minipage}{0.5\\linewidth}")
        print("\\begin{enumerate}")
        for ques in exer:
            if (i==6):
                print("\\end{enumerate}")
                print("\\end{minipage}")
                print("\\begin{minipage}{0.5\\linewidth}")
                print("\\begin{enumerate}\\setcounter{enumi}{5}")
            print("\\item $"+str(ques[0])+"x + "+str(ques[1])+"y$")
            i+=1
        print("\\end{enumerate}")
        print("\\end{minipage}")
        print("\\end{exo}")

def main():
    ListExer = []
    ListSol = []
    for i in range(EX):
        ListExer.append([])
        for j in range(QUES):
            ListExer[i].append(getCalc())
    print("\\documentclass{article}")
    print("\\usepackage{amsmath,amssymb,amsthm}")
    print("\\usepackage[svgnames]{xcolor}")
    print("\\usepackage[margin=1.5cm]{geometry}")
    print("\\newtheorem{exo}{Exercice}")
    print("\\theoremstyle{definition}")
    print("\\newtheorem{solution}{Solution}")
    print("\\begin{document}")
    printEnonce(ListExer)
    print("\\newpage")
    printSolution(ListExer)
    print("\\end{document}")

main()
