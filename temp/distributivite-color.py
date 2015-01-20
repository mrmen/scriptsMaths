#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 23-09-2013 21:34:02
#    Time-stamp: <13-01-2015 23:12:15>
#
#    File name : /tmp/distrib.py
#    Description : creation d'exercices pour la distributivite
#                  en cinquieme avec calcul litteral
#
# pour l'alea
import random
import sympy
import re

# nombre d'exos
EX=5
# nombre de calculs par exo
Q=10

# bornes pour les nombres dans les calculs
BorneMin=1
BorneMax=13

# signes possible dans la parenthese
sgn = ["+","-"]
# variable dispo
X = ["x","y","z",""]

ListExer = []
ListExerCool = []
# debut du document LaTeX
print("\\documentclass{article}\n\\usepackage{amsmath,amssymb,enumerate,xcolor}\n\\newtheorem{exo}{Exercice}\n\\newtheorem{solution}{Solution}\n\\usepackage[margin=1.5cm]{geometry}\n\\begin{document}")


for i in range(EX):
    # un exo + une minipage + enumerate[A]
    ListExer.append([])
    ListExerCool.append([])
    print("\\begin{exo}\\ \n\n\\begin{minipage}{0.5\\linewidth}\n\\begin{enumerate}[A]\n")
    for j in range(Q):
        # si i=5 passer sur l'autre cote de la page
        if j==5:
            # fermeture puis ouvertur
            print("\\end{enumerate}\n\\end{minipage}\n\\begin{minipage}{0.5\\linewidth}\n\\begin{enumerate}[A]\n\\setcounter{enumi}{5}\n")
        # preparation
        facteur = random.randint(BorneMin,BorneMax)
        elt1 = random.randint(BorneMin,BorneMax)
        isX1 = X[random.randint(0,len(X)-1)]
        isSgn = sgn[random.randint(0,len(sgn)-1)]
        elt2 = random.randint(BorneMin,BorneMax)
        isX2 = X[random.randint(0,len(X)-1)]
        # alea pour le facteur a gauche ou a droite
        ##
        ##
        ##
        tosolve = ""
        tosolve = tosolve + str(facteur) + "*("
        if (isX1==""):
            tosolve = tosolve + str(elt1)
        else:
            tosolve = tosolve + str(elt1) + "*" + str(isX1)
        tosolve = tosolve + isSgn
        if (isX2==""):
            tosolve = tosolve + str(elt2)
        else:
            tosolve = tosolve + str(elt2) + "*" + str(isX2)
        tosolve = tosolve + ")"
        ListExer[i].append(tosolve)
        ##
        ##
        ##
        if (random.randint(0,1000)%2):
            print("\\item $="+str(facteur)+"("+str(elt1)+isX1+isSgn+str(elt2)+isX2+")$")
            ListExerCool[i].append(str(facteur)+"("+str(elt1)+isX1+isSgn+str(elt2)+isX2+")")
        else:
            print("\\item $=("+str(elt1)+isX1+isSgn+str(elt2)+isX2+")"+str(facteur)+"$")
            ListExerCool[i].append("("+str(elt1)+isX1+isSgn+str(elt2)+isX2+")"+str(facteur))
    # et on ferme
    print("\\end{enumerate}\n\\end{minipage}\n\\end{exo}\n\\bigskip\n")

print("\\newpage")

def dothestuff(expr):
    SPLIT=[]
    temp=expr
    temp = temp.replace("*","")
    # decoupe facteur parent
    if temp[0]=="(":
        SPLIT=temp[1:].split(")")
    else:
        SPLIT=temp[:-1].split("(")
    # decoup elt parent
    SPLIT.sort(key=len, reverse=False)
    facteur=SPLIT[0]
    if "+" in SPLIT[1]:
        SPLIT2=SPLIT[1].split("+")
#        print(facteur+"*"+SPLIT2[0]+"+"+facteur+"*"+SPLIT2[1])
        return "{\\color{blue}"+facteur+"}{\\color{red}*}{\\color{green}"+SPLIT2[0]+"}+{\\color{blue}"+facteur+"}{\\color{red}*}{\\color{orange}"+SPLIT2[1]+"}"
    else:
        SPLIT2=SPLIT[1].split("-")
        return "{\\color{blue}"+facteur+"}{\\color{red}*}{\\color{green}"+SPLIT2[0]+"}-{\\color{blue}"+facteur+"}{\\color{red}*}{\\color{orange}"+SPLIT2[1]+"}"

def colorexpr(expr):
    pattern="([^\(\*]*)[\*]*\(([^\-\+]*)(.)([^\)]*)\)([^\(]*)"
    replaceBefore="{\\color{blue}\\1}{\\color{red}*}({\\color{green}\\2}\\3{\\color{orange}\\4})"
    replaceAfter="({\\color{green}\\2}\\3{\\color{orange}\\4}}){\\color{red}*}{\\color{blue}\\5})"
    if re.match("^[^\(]+",expr):
        return re.subn(pattern,replaceBefore,expr)[0]
    else:
        return re.subn(pattern,replaceAfter,expr)[0]

        

for i in range(EX):
    print("\\begin{solution}\\ \n\n\\begin{minipage}{0.5\\linewidth}\n\\begin{enumerate}[A]\n")
    for j in range(Q):
        if j==5:
            # fermeture puis ouverture
            print("\\end{enumerate}\n\\end{minipage}\n\\begin{minipage}{0.5\\linewidth}\n\\begin{enumerate}[A]\n\\setcounter{enumi}{5}\n")
        x = sympy.var('x')
        y = sympy.var('y')
        z = sympy.var('z')
        #        print("\\item $="+str(sympy.simplify(ListExer[i][j])).replace("*"," ")+"$")
        print("\\item \\begin{align*}")
        print("\\labelenumi ")
        print("&= "+ListExerCool[i][j].replace("*"," \\times ")+"\\\\")
        print("&= "+colorexpr(ListExer[i][j]).replace("*"," \\times ")+" \\\\")
        print("&= "+dothestuff(ListExer[i][j]).replace("*"," \\times "))
        print("\\\\")
        print("&="+str(sympy.simplify(ListExer[i][j])).replace("*"," ")+"\\\\")
        print("\\end{align*}")
# et on ferme
    print("\\end{enumerate}\n\\end{minipage}\n\\end{solution}\n\\bigskip\n")

# et on cloture
print("\\end{document}")

# et on a gagne
