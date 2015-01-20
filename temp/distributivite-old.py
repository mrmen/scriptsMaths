#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 23-09-2013 21:34:02
#    Time-stamp: <17-12-2013 12:53:59>
#
#    File name : /tmp/distrib.py
#    Description : creation d'exercices pour la distributivite
#                  en cinquieme avec calcul litteral
#
# pour l'alea
import random
import sympy

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

# debut du document LaTeX
print("\\documentclass{article}\n\\usepackage{amsmath,amssymb,enumerate}\n\\newtheorem{exo}{Exercice}\n\\newtheorem{solution}{Solution}\n\\usepackage[margin=1.5cm]{geometry}\n\\begin{document}")


for i in range(EX):
    # un exo + une minipage + enumerate[A]
    ListExer.append([])
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
        else:
            print("\\item $=("+str(elt1)+isX1+isSgn+str(elt2)+isX2+")"+str(facteur)+"$")
    # et on ferme
    print("\\end{enumerate}\n\\end{minipage}\n\\end{exo}\n\\bigskip\n")

print("\\newpage")

for i in range(EX):
    print("\\begin{solution}\\ \n\n\\begin{minipage}{0.5\\linewidth}\n\\begin{enumerate}[A]\n")
    for j in range(Q):
        if j==5:
            # fermeture puis ouverture
            print("\\end{enumerate}\n\\end{minipage}\n\\begin{minipage}{0.5\\linewidth}\n\\begin{enumerate}[A]\n\\setcounter{enumi}{5}\n")
        x = sympy.var('x')
        y = sympy.var('y')
        z = sympy.var('z')
        print("\\item $="+str(sympy.simplify(ListExer[i][j])).replace("*"," ")+"$")
    # et on ferme
    print("\\end{enumerate}\n\\end{minipage}\n\\end{solution}\n\\bigskip\n")

# et on cloture
print("\\end{document}")

# et on a gagne
