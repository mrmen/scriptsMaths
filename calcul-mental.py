# /usr/bin/python
# -*- coding:utf8 -*-


def print_exercice(ex_type):
    if ex_type == "addition":
        a = random.randint(10,50)
        b = random.randint(10,50)
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
        question = ['Quelles est la difference de %s et %s ?', 'A %s, retranche %s.', '%s - %s'][random.randint(0,2)]%(a,b)
        return '''
        \\begin{frame}{Soustraction}
        \centering
        %s
        \end{frame}'''%(question)
    elif ex_type == "multiplication":
        a = random.randint(2,9)
        b = random.randint(2,9)
        question = ['Quelles est le produit de %s et %s ?', 'Multiplie %s par %s.', '%s $\\times$ %s'][random.randint(0,2)]%(a,b)
        return '''
        \\begin{frame}{Multiplication}
        \centering
        %s
        \end{frame}'''%(question)
    elif ex_type == "fractions":
        a = [random.randint(2,9) for _ in range(4)]
        sign =['\\times ', '+', '-', '\\div '][random.randint(0,3)]
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
        \\begin{tabular}{|c|c|}
        \hline
        %s & %s\\\\
        \hline
        %s & ?\\\\
        \hline
        \end{tabular}
        \\textbf{Compléte ce tableau de proportionnalité.}
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
        \[ %s %s %s\]
        \\textbf{Quel est le résultat du calcul précédent ?}
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
        \end{frame}'''%(L[0],L[1],L[2])
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
        
        \\tkzMarkRightAngle(A,B,C)
        
        \\tkzLabelSegment[below](A,B){%s}
        \\tkzLabelSegment[right](B,C){%s}
        \\tkzLabelSegment[left](C,A){%s}
        \end{tikzpicture}
        
        \\textbf{Ce triangle est-il rectangle ?}
        \end{frame}'''%(L[0],L[1],L[2])


        
        
import os, sys, clipboard, webbrowser
import random
        
if len(sys.argv)<2:
    print("Erreur il manque un argument.")
    sys.exit(1)

string='''\documentclass{beamer}
\\usetheme{Warsaw}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage{tkz-euclide}
\\usetkzobj{all}
\\begin{document}'''

    
liste_exercice = sys.argv[1:]
for ex_type in liste_exercice:
    string+=print_exercice(ex_type)
                
string+='''\end{document}'''
clipboard.set(string)

webbrowser.open('texwriter://')
