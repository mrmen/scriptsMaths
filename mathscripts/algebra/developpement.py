__author__ = 'mrmen'

from TemplateExercice import *
import random
from sympy import expand


class Developpement(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = -10
        self.max = 10
        self.nb = ["x", "y", ""]
        self.sign = ["\\times"]
        self.additive = ["+", "-"]
        self.generate()

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
                # create list with [value, exp]
                nbnumbers = 4
                values = []
                for _ in range(nbnumbers):
                    value = self.random_except_zero()
                    if (_==0) or (_==2):
                        values.append([value, self.nb[random.randint(0,len(self.nb)-1)], self.additive[random.randint(0,1)]])
                    else:
                        values.append([value, self.nb[random.randint(0,len(self.nb)-1)]])
                tempenonce.append(self.format_enonce(values))
                tempsolution.append(self.format_solution(values))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)

    def format_enonce(self, liste):
        string = []
        for elt in liste:
            fact = elt[0]
            if (fact < 0):
                fact = "(" + str(fact) + ")"
            variable = elt[1]
            if (len(elt)==3):
                variable += elt[2]
            if (variable == "+") or (variable == "-") or (variable==""):
                string.append(str(fact) + variable)
            else:
                string.append(str(fact) + " \\times " + str(variable))
        return self.concat_enonce(string)

    def concat_enonce(self, liste):
        count = 0
        string = "\\bigg("
        for elt in liste:
            string += elt+" "
            count +=1
            if count == 2:
                string+="\\bigg)\\times\\bigg("
        string+="\\bigg)"
        return "$" + string + "$"

    def format_solution(self, liste):
        calc_initial = self.format_enonce(liste).replace("$", "")
        calc = calc_initial.replace("\\times", "*").replace("\\bigg","")
        calc_out = str(expand(calc))
        return "$"+str(calc_initial)+" = "+calc_out+"$"


if __name__ == "__main__":
    app = Developpement()
    app.display()
