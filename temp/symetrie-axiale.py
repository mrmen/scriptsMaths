import random
import math

# nombre de sommets de la figure
SOMMET = 6
LETTRE = []
for i in range(6):
    LETTRE.append(chr(65 + i))

# genere une liste de coordonees pour les sommets
L = []
for i in range(SOMMET):
    x = random.randint(-5,5)
    y = random.randint(-5,5)
    while [x,y] in L:
        x = random.randint(-5,5)
        y = random.randint(-5,5)
    L.append([x,y])

# trouve les extrema des abscisses pour tracer l'axe de symetrie
ABS = []
ORD = []
for i in L:
    ABS.append(i[0])
    ORD.append(i[1])
ABS.sort()
ORD.sort()

MIN = ABS[0]
MAX = ABS[len(ABS)-1]
ORD_MIN = ORD[0]
ORD_MAX = ORD[len(ORD)-1]

# genere les coefficients de l'axe de symetrie
EQNC = []
EQNC.append(random.randint(-3,4))
EQNC.append(random.randint(-3,4))
a=EQNC[0]
#ORD_MAX = max(ORD_MAX, a*ORD_MAX+EQNC[1])

PLOT_DOMAIN = []
if a<0:
    PLOT_DOMAIN.append(float(ORD_MAX - EQNC[1])/a)
    PLOT_DOMAIN.append(float(ORD_MIN - EQNC[1])/a)
if a>0:
    PLOT_DOMAIN.append(float(ORD_MIN - EQNC[1])/a)
    PLOT_DOMAIN.append(float(ORD_MAX - EQNC[1])/a)
if a==0:
    PLOT_DOMAIN.append(MIN)
    PLOT_DOMAIN.append(MAX)
###
##
#
# Commence l'ecriture sur la stdout
#
##
###
print("\\documentclass{article}")
print("\\usepackage{tikz}")
print("\\usepackage[margin=1cm]{geometry}")
print("\\begin{document}")

print("\\vfill\\begin{center}\\begin{tikzpicture}[line cap = round, join = round]")

###
##
#
# create string for polygon
#
##
###
print("\\draw[line width=0.5pt, color = gray!30] ("+str(MIN)+","+str(ORD_MIN)+") grid ("+str(MAX)+","+str(ORD_MAX)+ ");")

string = ""
idx = 0
for i in L:
    string = string + "-- (" + str(i[0]) + "," + str(i[1]) + ")"
    print("\\fill ("+str(i[0])+","+str(i[1])+") circle (1.5pt)node[left]{"+LETTRE[idx]+"};")
    idx+=1

print("\\draw[color = black, line width=1pt]" + string[2:] + "-- cycle;")
# if EQNC[1]<0:
#     print("\\draw[color = red, line width=2pt] plot[domain="+str(MIN)+":"+str(MAX)+"] (\\x," + str(EQNC[0]) + "*\\x " + str(EQNC[1]) +");")
# else:
print("\\draw[color = red, line width=2pt] plot[domain="+str(PLOT_DOMAIN[0])+":"+str(PLOT_DOMAIN[1])+"] (\\x," + str(EQNC[0]) + "*\\x + " + str(EQNC[1]) +");")
    
print("\\end{tikzpicture}\\end{center}\\vfill")
#####
#####
#####


###
##
print("\\newpage")
##
###


SYM = []
n = float(1 + a**2)
c = -EQNC[1]
for point in L:
    cm = a*point[0] - point[1]
    xm = point[0] + 2* a* ( c - cm)/n
    ym = point[1] + 2 * (-1) * (c-cm)/n
    SYM.append([xm,ym])

for i in range(len(L)):
    MIN = min(SYM[i][0],MIN)
    ORD_MIN = min(SYM[i][1],ORD_MIN)
    MAX = max(SYM[i][0],MAX)
    ORD_MAX = max(SYM[i][1],ORD_MAX)

print("\\vfill\\begin{center}\\begin{tikzpicture}")

###
##
#
# create string for polygon
#
##
###
print("\\draw[line width = 0.5pt, color = gray!30] ("+str(MIN)+","+str(ORD_MIN)+") grid ("+str(MAX)+","+str(ORD_MAX)+ ");")
#####
# Initiale
#####
string = ""
idx = 0
for i in L:
    string = string + "-- (" + str(i[0]) + "," + str(i[1]) + ")"
    print("\\fill ("+str(i[0])+","+str(i[1])+") circle (1.5pt)node[left]{"+LETTRE[idx]+"};")
    idx+=1

print("\\draw[color = black, line width=1pt]" + string[2:] + "--cycle;")
print("\\draw[color = red, line width=2pt] plot[domain="+str(PLOT_DOMAIN[0])+":"+str(PLOT_DOMAIN[1])+"] (\\x," + str(EQNC[0]) + "*\\x + " + str(EQNC[1]) +");")
####
# Finale
####
string = ""
idx = 0
for i in SYM:
    string = string + "-- (" + str(i[0]) + "," + str(i[1]) + ")"
    print("\\fill ("+str(i[0])+","+str(i[1])+") circle (1.5pt)node[right]{"+LETTRE[idx]+"'};")
    idx+=1

print("\\draw[ color = blue, line width = 1pt]" + string[2:] + "--cycle;")

for i in range(len(SYM)):
    print("\\draw[style = dashed, color = gray!20, line width = 0.5pt] (" + str(L[i][0]) + "," + str(L[i][1]) + ") -- (" + str(SYM[i][0]) + "," + str(SYM[i][1]) + ");")



print("\\end{tikzpicture}\\end{center}\\vfill")

print("\\end{document}")
