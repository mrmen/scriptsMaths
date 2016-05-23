__author__ = 'mrmen'

from TemplateExercice import *
import random
from sympy import solve


class Developpement(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = -10
        self.max = 10
        self.generate()
        self.COLONNE=0

    def random_except_zero(self):
        x = 0
        while (x==0):
            x = random.randint(self.min, self.max)
        return x

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                lmember, rmember = [], []
                for liste in lmember, rmember:
                    temp = []
                    for _ in range(2):
                        a = self.random_except_zero()
                        if a<0:
                            a="("+str(a)+")"
                        b = self.random_except_zero()
                        if b<0:
                            b="("+str(b)+")"
                        if random.randint(0,1):
                            denom = random.randint(1,9)
                        else:
                            denom = 1
                        temp = [[str(a),"*", "x", "+",str(b)],[str(denom)]]
                        liste.append(temp)
                tempenonce.append(self.format_enonce(lmember,rmember))
                tempsolution.append(self.format_solution(lmember,rmember))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)

    def concat_elements(self, lmember, rmember):
        stringleft , stringright = [], []
        for element in lmember:
            string = ""
            string = "".join(element[0])
            if element[1] != 1:
                string = "\\dfrac{"+string+"}{"+element[1][0]+"}"
            stringleft.append(string)
        for element in rmember:
            string = ""
            string = " ".join(element[0])
            if element[1] != 1:
                string = "\\dfrac{"+string+"}{"+element[1][0]+"}"
            stringright.append(string)
        return "+".join(stringleft)+"="+"+".join(stringright)

    def format_enonce(self, lmember, rmember):
        string = self.concat_elements(lmember, rmember)
        return "$"+string.replace("*"," \\times ")+"$"

    def format_solution(self, lmember, rmember):
        string = self.concat_elements(lmember, rmember)
        string = string.replace("=","-(")
        string = string + ")"
        calc = string.replace("\\dfrac{","(").replace("}{",")/(").replace("}",")")
        calc_out = str(solve(calc,"x"))
        solution = calc_out[1:-1]
        if "/" in solution:
            solution = "\\dfrac{"+solution.replace("/","}{")+"}"
        return "$"+solution+"$"


if __name__ == "__main__":
    app = Developpement()
    app.display()
