#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 05-02-2014 11:25:58
#    Time-stamp: <05-02-2014 12:34:16>
#
#    File name : /tmp/fractions.py
#    Description :
#

import random

FACTEUR = [2,3,4,5,6,7,8,9,10,11,12,13]
NUMERATEUR = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
DENOMINATEUR = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

EXER = 5
QUES = 10

FEUILLE = []

def getExer():
    numerateur = []
    numerateur.append(NUMERATEUR[random.randint(0,len(NUMERATEUR)-1)])
    numerateur.append(NUMERATEUR[random.randint(0,len(NUMERATEUR)-1)])

    denominateur = []
    denominateur.append(DENOMINATEUR[random.randint(0,len(DENOMINATEUR)-1)])

    facteur = FACTEUR[random.randint(0,len(FACTEUR)-1)]
    denominateur.append(denominateur[0]*facteur)
    return [numerateur,denominateur]

def parserExer(list):
    numerateur = list[0]
    denominateur = list[1]
    #
    frac = []
    frac.append("\\dfrac{"+str(numerateur[0])+"}"+"{"+str(denominateur[0])+"}")
    frac.append("\\dfrac{"+str(numerateur[1])+"}"+"{"+str(denominateur[1])+"}")
    return frac


def getSol(list):
    numerateur = list[0]
    denominateur = list[1]
    facteur = int(list[1][1]/list[1][0])
    stringOutput = ""
    stringOutput = stringOutput + "\\begin{align*}"
    frac = parserExer(list)

    stringOutput += frac[0] +"+"+frac[1]

    stringOutput +="\n& = "
    fracTimes = frac[0].replace("}","{\color{red}\\times "+str(facteur)+"}}")
    stringOutput += fracTimes + "+" + frac[1]
    stringOutput += "\\\\\n & = "

    fracTimes = "\\dfrac{"+str(numerateur[0]*facteur)+"}{{\color{red}"+str(denominateur[1])+"}}"
    stringOutput += fracTimes + "+" + "\\dfrac{"+str(numerateur[1])+"}"+"{\color{red}"+str(denominateur[1])+"}"
    stringOutput += "\\\\\n & = "

    result = "\\dfrac{"+str(numerateur[0]*facteur + numerateur[1])+"}{"+str(denominateur[1])+"}"
    stringOutput += result+"\n"
    stringOutput += "\\end{align*}"
    
    return stringOutput
      
    
def genFeuille(list):
    print("\\documentclass[12pt]{article}\n\\usepackage{amsmath,amsmath,xcolor}\n\n")
    print("\\usepackage[margin=1.5cm]{geometry}")
    print("\\newtheorem{exercice}{Exercice}")
    print("\\newtheorem{solution}{Solution}")
    print("\\begin{document}")
    for exercice in FEUILLE:
        print("\\begin{exercice}\ \n\n")
        print("\\begin{minipage}{0.5\\linewidth}\\centering")
        print("\\begin{enumerate}\n")
        i = 1
        for question in exercice:
            frac = parserExer(question)
            print("\\item $"+frac[0]+"+"+frac[1]+"$")
            i+=1
            if (i==6):
                print("\\end{enumerate}")
                print("\\end{minipage}")
                print("\\begin{minipage}{0.5\\linewidth}\\centering")
                print("\\begin{enumerate}\\setcounter{enumi}{5}")
        print("\\end{enumerate}")
        print("\\end{minipage}")
        print("\\end{exercice}")


    for exercice in FEUILLE:
        print("\n\\newpage\n")
        print("\\begin{solution}\ \n\n")
        print("\\begin{minipage}{0.5\\linewidth}\\centering")
        print("\\begin{enumerate}")
        i = 1
        for question in exercice:
            output = getSol(question)
            print("\\item" + output)
            i+=1
            if (i==6):
                print("\\end{enumerate}")
                print("\\end{minipage}")
                print("\\begin{minipage}{0.5\\linewidth}\\centering")
                print("\\begin{enumerate}\\setcounter{enumi}{5}")
        print("\\end{enumerate}")
        print("\\end{minipage}")
        print("\\end{solution}")


    print("\\end{document}")

        
        

def main():
    for exercice in range(EXER):
        ListQuestion = []
        for question in range(QUES):
            # done with two steps for debug
            temp = getExer()
            ListQuestion.append(temp)
        FEUILLE.append(ListQuestion)
    genFeuille(FEUILLE)

main()
