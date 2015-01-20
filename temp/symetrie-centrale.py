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

# MIN = ABS[0]
# MAX = ABS[len(ABS)-1]
# ORD_MIN = ORD[0]
# ORD_MAX = ORD[len(ORD)-1]
MIN = -15
MAX = 15
ORD_MIN = -15
ORD_MAX = 15


  


# trouver un point de symetrie
POINT = [random.randint(-5,5), random.randint(-5,5)]

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

print("\\vfill\\begin{center}\\begin{tikzpicture}[line cap = round, join = round, scale=0.75]")

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

print("\\fill[color = red] ("+str(POINT[0])+","+str(POINT[1])+") circle (1.5pt) node[left]{$O$};")
    
print("\\end{tikzpicture}\\end{center}\\vfill")
#####
#####
#####


###
##
print("\\newpage")
##
###

print("\\vfill\\begin{center}\\begin{tikzpicture}[scale = 0.75]")

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
####
# Finale
####
string = ""
idx = 0
for i in L:
    string = string + "-- (" + str(i[0]) + "," + str(i[1]) + ")"
    print("\\fill ("+str(i[0])+","+str(i[1])+") circle (1.5pt)node[left]{"+LETTRE[idx]+"};")
    idx+=1

idx = 0
for i in L:
    string = string + "-- (" + str(i[0]) + "," + str(i[1]) + ")"
    print("\\fill[rotate around={180:("+str(POINT[0])+","+str(POINT[1])+")}] ("+str(i[0])+","+str(i[1])+") circle (1.5pt)node[left]{"+LETTRE[idx]+"'};")
    idx+=1


print("\\draw[color = blue, line width=1pt,rotate around={180:("+str(POINT[0])+","+str(POINT[1])+")}]" + string[2:] + "--cycle;")

for i in L:
    print("\\draw[style = dashed, color = purple!20, line width = 0.5pt] (" + str(i[0]) + "," + str(i[1]) + ") -- (" + str(POINT[0]) + "," + str(POINT[1]) + ");")
    print("\\draw[style = dashed, color = purple!20, line width = 0.5pt, rotate around={180:("+str(POINT[0])+","+str(POINT[1])+")}] (" + str(i[0]) + "," + str(i[1]) + ") -- (" + str(POINT[0]) + "," + str(POINT[1]) + ");")

print("\\fill[color = red] ("+str(POINT[0])+","+str(POINT[1])+") circle (1.5pt) node[left]{$O$};")

print("\\end{tikzpicture}\\end{center}\\vfill")

print("\\end{document}")
