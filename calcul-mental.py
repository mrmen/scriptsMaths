# /usr/bin/python
# -*- coding:utf8 -*-
import sys, random

def print_exercice(ex_type):
    global answers
    if ex_type == "addition":
        a = random.randint(10,50)
        b = random.randint(10,50)
        answers+=[[str(a)+"+"+str(b),"=",a+b]]
        question = ['Quelles est la somme de %s et %s ?', 'Ajouter %s à %s.', '%s +%s'][random.randint(0,2)]%(a,b)
        return '''
        \\begin{frame}{Addition}
        \centering
        %s
        \end{frame}'''%(question)
    elif ex_type == "soustraction":
        a = random.randint(10,50)
        b = random.randint(10,50)
        a,b = max(a,b), min(a,b)
        answers+=[[str(a)+"-"+str(b),"=",a-b]]
        question = ['Quelles est la difference de %s et %s ?', 'A %s, retranche %s.', '%s - %s'][random.randint(0,2)]%(a,b)
        return '''
        \\begin{frame}{Soustraction}
        \centering
        %s
        \end{frame}'''%(question)
    elif ex_type == "multiplication":
        a = random.randint(2,9)
        b = random.randint(2,9)
        answers+=[[str(a)+"\\times"+str(b),"=",a*b]]
        question = ['Quelles est le produit de %s et %s ?', 'Multiplie %s par %s.', '%s $\\times$ %s'][random.randint(0,2)]%(a,b)
        return '''
        \\begin{frame}{Multiplication}
        \centering
        %s
        \end{frame}'''%(question)
    elif ex_type == "fractionssimp":
        a = random.randint(2,9)
        b = random.randint(2,9)*a
        answers+=[["\\dfrac{%s}{%s}"%(a,b),"=","\\dfrac{%s}{%s}"%(1,int(b/a))]]
        return '''
        \\begin{frame}{Fractions}
        Simplifie
        \centering
        \[\dfrac{%s}{%s}\]
        \end{frame}'''%(a,b)
    elif ex_type == "fractionscomp":
        a = [random.randint(2,9) for _ in range(4)]
        answers+=[["\\dfrac{%s}{%s} = \\dfrac{%s}{%s}"%(a[0],a[1], a[0]*a[3],a[1]*a[3]),"\\dots","\\dfrac{%s}{%s} = \\dfrac{%s}{%s}"%(a[2],a[3], a[2]*a[1],a[3]*a[1])]]
        return '''
        \\begin{frame}{Fractions}
        Compare
        \centering
        \[\dfrac{%s}{%s}\ et\ \dfrac{%s}{%s}\]
        \end{frame}'''%(a[0],a[1],a[2],a[3])
    elif ex_type == "fractionsadd":
        a = [random.randint(2,9) for _ in range(4)]
        sign =['+', '-'][random.randint(0,1)]
        answers+=[["","",""]]
        return '''
        \\begin{frame}{Fractions}
        \centering
        \[\dfrac{%s}{%s} %s \dfrac{%s}{%s}\]
        \end{frame}'''%(a[0],a[1],sign,a[2],a[3])
    elif ex_type == "fractionsall":
        a = [random.randint(2,9) for _ in range(4)]
        sign =['\\times ', '+', '-', '\\div '][random.randint(0,3)]
        answers+=[["","",""]]
        return '''
        \\begin{frame}{Fractions}
        \centering
        \[\dfrac{%s}{%s} %s \dfrac{%s}{%s}\]
        \end{frame}'''%(a[0],a[1],sign,a[2],a[3])
    elif ex_type == "proportionnalite":
        a = random.randint(1,9)
        b = random.randint(1,9)
        facteur = random.randint(1,9)
        return '''
        \\begin{frame}{Proportionnalité}
        \centering
        \\textbf{Complète ce tableau de proportionnalité.}
        \\begin{tabular}{|c|c|}
        \hline
        %s & %s\\\\
        \hline
        %s & ?\\\\
        \hline
        \end{tabular}
        \end{frame}'''%(a,a*facteur,b)
    elif ex_type == "relatifs":
        a = 0
        while a==0:
            a = random.randint(-10,10)
        b = "("+str(random.randint(-20,-1))+")"
        sgn = ["+","-"][random.randint(0,1)]
        return '''
        \\begin{frame}{Relatifs}
        \centering
        \\textbf{Quel est le résultat de ce calcul ?}
        \[ %s %s %s\]
        \end{frame}'''%(a,sgn,b)
    elif ex_type == "fonction":
        a = random.randint(-10,10)
        b = random.randint(1,10)
        sgn = ["+","-"][random.randint(0,1)]
        valeur = random.randint(-3,4)
        return '''
        \\begin{frame}{Fonctions}
        \centering
        \[ f : x \mapsto %s\\times x %s %s\]
        \\textbf{Quel est l'image de %s par la fonction f ?}
        \end{frame}'''%(a,sgn,b,valeur)
    elif ex_type=="perimetre":
        a = random.randint(2,20)
        b = random.randint(2,20)
        mark_type = ["|","||"][random.randint(0,1)]
        if mark_type == "||":
            b = ""
        return '''
        \\begin{frame}{Périmètre}
        \centering
        \\begin{tikzpicture}
        \\tkzDefPoint(0,0){A}
        \\tkzDefPoint(0,3){B}
        \\tkzDefPoint(3,3){C}
        \\tkzDefPoint(3,0,){D}

        \\tkzMarkSegments[mark=||](A,B C,D)
        \\tkzMarkSegments[mark=%s](A,D B,C)
        \\tkzMarkRightAngle(A,B,C)
        \\tkzLabelSegment[left](A,B){%s}

        \\tkzLabelSegment[above](B,C){%s}

        \\tkzLabelPoints(A,B,C,D)
        \\tkzDrawPolygon(A,B,C,D)
        \end{tikzpicture}

        \\textbf{Quel est le périmètre de cette figure ?}
        \end{frame}'''%(mark_type,a,b)
    elif ex_type == "aire":
        a = random.randint(2,20)
        b = random.randint(2,20)
        mark_type = ["|","||"][random.randint(0,1)]
        if mark_type == "||":
            b = ""
        return '''
        \\begin{frame}{Aire}
        \centering
        \\begin{tikzpicture}
        \\tkzDefPoint(0,0){A}
        \\tkzDefPoint(0,3){B}
        \\tkzDefPoint(3,3){C}
        \\tkzDefPoint(3,0,){D}

        \\tkzMarkSegments[mark=||](A,B C,D)
        \\tkzMarkSegments[mark=%s](A,D B,C)
        \\tkzMarkRightAngle(A,B,C)

        \\tkzLabelSegment[left](A,B){%s}

        \\tkzLabelSegment[above](B,C){%s}

        \\tkzLabelPoints(A,B,C,D)
        \\tkzDrawPolygon(A,B,C,D)
        \end{tikzpicture}
        \\textbf{Quel est l'aire de cette figure ?}
        \end{frame}'''%(mark_type,a,b)
    elif ex_type == "pythagore":
        L = []
        L.append(random.randint(1,9))
        L.append(random.randint(1,9))
        temp=max(L)
        L.append("")
        random.shuffle(L)
        return '''
        \\begin{frame}{Pythagore (direct)}
        \centering
        \\begin{tikzpicture}
        \\tkzDefPoint(0,0){A}
        \\tkzDefPoint(3,0){B}
        \\tkzDefPoint(3,4){C}
        \\tkzDrawPolygon(A,B,C)
        \\tkzLabelPoints(A,B,C)

        \\tkzMarkRightAngle(A,B,C)

        \\tkzLabelSegment[below](A,B){%s}
        \\tkzLabelSegment[right](B,C){%s}
        \\tkzLabelSegment[left](C,A){%s}
        \end{tikzpicture}

        \\textbf{Quelle est la mesure du côté manquant ?}
        \end{frame}'''%(L[0],min(L[1],L[2]),max(L[1],L[2]))
    elif ex_type == "pythagore-reciproque":
        L = []
        u = random.randint(1, 10)
        v = random.randint(1, 10)
        v, u = min(u, v), max(u, v)
        L = [u ** 2 - v ** 2, 2 * u * v, u ** 2 + v ** 2]
        #random.shuffle(L)
        return '''
        \\begin{frame}{Pythagore (réciproque)}
        \centering
        \\begin{tikzpicture}
        \\tkzDefPoint(0,0){A}
        \\tkzDefPoint(3,0){B}
        \\tkzDefPoint(3,4){C}
        \\tkzDrawPolygon(A,B,C)
        \\tkzLabelPoints(A,B,C)

        \\tkzLabelSegment[below](A,B){%s}
        \\tkzLabelSegment[right](B,C){%s}
        \\tkzLabelSegment[left](C,A){%s}
        \end{tikzpicture}

        \\textbf{Ce triangle est-il rectangle ?}
        \end{frame}'''%(L[0],L[1],L[2])




import os, sys, random
if sys.platform == "ios":
    import clipboard, webbrowser

if len(sys.argv)<2:
    print("Erreur il manque un argument.")
    sys.exit(1)

string='''\documentclass{beamer}
\\usetheme{Warsaw}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage{tkz-euclide}
%\\usetkzobj{all}
\\begin{document}'''

liste_sixieme = ["addition", "soustraction", "multiplication"]
liste_troisieme = ["fractionssimp","fractionscomp","fractionsadd"]
answers = []
correction = 0

liste_exercice = sys.argv[1:]
if "6eme" in liste_exercice:
    liste_exercice = random.sample(liste_sixieme, len(liste_sixieme))
    correction = 1
if "3eme" in liste_exercice:
    liste_exercice = random.sample(liste_troisieme, len(liste_troisieme))
    correction = 1
for ex_type in liste_exercice:
    string+=print_exercice(ex_type)

if correction == 1:
    string+='''\\begin{frame}{Corrections}'''
    for a in answers:
        string+='''\\begin{block}<+->{}$ '''+a[0]+a[1]+str(a[2])+'''$\\end{block}'''
    string+='''\\end{frame}'''

string+='''\end{document}'''
print("%",answers)

if sys.platform == "ios":
    clipboard.set(string)
    webbrowser.open('texwriter://')
else:
    print(string)
