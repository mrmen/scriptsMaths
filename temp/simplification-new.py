import random

L=[]
VAR=['','x','y','z']


def pprint(L,VAR):
    string = ""
    COLOR=["blue","red","green","black"]
    for index in range(len(VAR)):
        for monome in L[index]:
            if monome > 0:
                string += "+"+str(monome)+VAR[index]+" "
            elif monome < 0:
                string += "+("+str(monome)+VAR[index]+") "
            else:
                1#nothing to do
    print("& = "+string[1:]+"\\\\")

def pprintExo(L,VAR):
    tempList = []
    for index in range(len(VAR)):
        for monome in L[index]:
            if monome > 0:
                temp = str(monome)+VAR[index]
            elif monome < 0:
                temp= "("+str(monome)+VAR[index]+")"
            else:
                1#nothing to do
            tempList.append(temp)
    random.shuffle(tempList)
    string = ""
    for monome in tempList:
        string += "+"+monome+" "
    print(string[1:])


def boucle(L,VAR):
    index=0
    print("\\begin{align*}")
    pprintExo(L,VAR)
    while index!=len(L):
        while len(L[index])!=1:
            temp=L[index].pop(0)
            L[index][0] = L[index][0] + temp
            pprint(L,VAR)
        index+=1
    print("\\end{align*}")


# exercice
ListExer = []
for exer in range(EXER):
    ListExer.append([])
    for question in range(QUESTION):
        polynome = []
        for index in range(len(VAR)):
            L.append([])
            for i in range(3):
                L[index].append(random.randint(-10,10))


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
