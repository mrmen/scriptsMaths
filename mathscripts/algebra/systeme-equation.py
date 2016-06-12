# coding: utf-8
# coding: utf-8
#__author__ = 'mrmen'

from TemplateExercice import *
import random
from sympy import solve_linear_system, Matrix
from sympy.abc import x,y


class SystemeEquation(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = -10
        self.max = 10
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                a1 = random.randint(self.min, self.max)
                b1 = random.randint(self.min, self.max)
                c1 = random.randint(self.min, self.max)
                a2 = random.randint(self.min, self.max)
                b2 = random.randint(self.min, self.max)
                c2 = random.randint(self.min, self.max)
                for nb in a1, b1, c1, a2, b2, c2:
                    if nb <0:
                        nb = '('+str(nb)+')'
                    else:
                        nb = str(nb)
                tempenonce.append(self.formatenonce(a1, b1, c1, a2, b2, c2))
                tempsolution.append(self.formatsolution(a1, b1, c1, a2, b2, c2))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)
    def formatenonce(self, a1, b1, c1, a2, b2, c2):
        string = '$\\left\\{\\begin{array}{ccc}'
        string += '%s x + %s y & = & %s\\\\' % (a1, b1, c1)
        string += '%s x + %s y & = & %s' % (a2, b2, c2)
        string += '\\end{array}\\right.$'
        return string

    def formatsolution(self, a1, b1, c1, a2, b2, c2):
        M = Matrix(((a1, b1, c1), (a2, b2, c2)))
        resultat = solve_linear_system(M, x, y)
        return '$'+str(resultat)+'$'

if __name__ == "__main__":
    app = SystemeEquation()
    app.display()