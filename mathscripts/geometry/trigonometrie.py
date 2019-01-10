__author__ = 'mrmen'

import random
import math

from TemplateExercice import *

# in order to use degres
def cos(angle):
    return math.cos(angle * math.pi / 180)
def sin(angle):
    return math.sin(angle * math.pi / 180)


class Trigonometrie(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.COLONNE=0
        self.min = 10
        self.max = 100
        self.value_added = [0, 1]
        self.alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                name = self.create_name()
                min_len = 2
                max_len = 10
                value = [round(random.uniform(min_len,max_len),1),round(random.uniform(min_len,max_len),1)]
                rect = random.randint(0, 2)
                tempenonce.append(self.create_enonce(name, value, rect))
            self.listeEnonce.append(tempenonce)

    def create_name(self):
        alphabet = list(self.alphabet)
        name = []
        for _ in range(3):
            index = random.randint(0, len(alphabet) - 1)
            name.append(alphabet.pop(index))
        return name

    def create_enonce(self, name, value, rect):
        name_temp = list(name)
        string_output = ""
        string_output += "Soit un triangle $%s%s%s$ rectangle en $%s$ tel que :" % (name[0], name[1], name[2], name[rect])
        main_sommet = name_temp.pop(rect)
        hyp = name_temp[0] + name_temp[1]
        c1 = main_sommet + name_temp.pop()
        c2 = main_sommet + name_temp.pop()
        m = min(value)
        M = max(value)
        anglename = list(name)
        d1 = anglename.pop(rect)
        s = anglename.pop(random.randint(0,1))
        d2 = anglename.pop()
        alpha = d1 + s + d2
        angle = random.randint(10,89)
        solution1 = "Il faut utiliser "
        if random.randint(0,2)==1:
            string_output += "\\[%s = %s~cm\ \\qquad \ %s = %scm\\ et\\ \\widehat{%s} = %s\degres\\]" % (hyp, M, c2, m, alpha, angle)
            if s in c1:
                self.currentSolution = ["cos", c1, angle, alpha, hyp, M]
                solution1 += "cosinus"
                solution2 = c1 + " = " + str(round(M*cos(angle), 1))
            else:
                self.currentSolution = ["sin", c1, angle, alpha, hyp, M]
                solution1 += "sinus"
                solution2 = c1 + " = " + str(round(M*sin(angle), 1))
        else:
            string_output += "\\[%s = %s~cm\ \\qquad \ %s = %scm\\ et\\ \\widehat{%s} = %s\degres\\]" % (c1, M, c2, m, alpha, angle)
            self.currentSolution = ["sin", hyp, angle, alpha, c1, M]
            if s in c1:
                solution1 += "cosinus"
                solution2 = hyp + " = " + str(round(M/cos(angle), 1))
            else:
                solution1 += "sinus"
                solution2 = c1 + " = " + str(round(M/sin(angle), 1))
        string_output += "Quelle est la longueur du côté manquant ?\n\n"
        string_output += "\\begin{minipage}{0.4\\linewidth}"
        string_output += "\\begin{flushleft}indice : \\qrcode{"+solution1+"}\\end{flushleft}"
        string_output += "\\end{minipage}\\begin{minipage}{0.4\\linewidth}"
        string_output += "\\begin{flushright}solution : \\qrcode{"+solution2+"}\\end{flushright}"
        string_output += "\\end{minipage}\n"
        return string_output


if __name__ == "__main__":
    app = Trigonometrie()
    app.display()
