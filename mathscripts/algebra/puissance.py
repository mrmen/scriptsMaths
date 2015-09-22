__author__ = 'mrmen'

from TemplateExercice import *
import random
from sympy import abc, simplify


class AdditionDecimaux(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = -10
        self.max = 10
        self.nb = ["a", "b", "c", "d"]
        self.sign = ["+", "-", "\\times", "\\div"]
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                # create list with [value, exp]
                nbnumbers = 5
                values = []
                for _ in range(nbnumbers):
                    exponent = random.randint(self.min, self.max)
                    value = self.nb[random.randint(0,len(self.nb)-1)]
                    values.append([value, exponent])
                signs = []
                for _ in range(nbnumbers-1):
                    signs.append(self.sign[random.randint(0,len(self.sign)-1)])
                #
                tempenonce.append(self.format_enonce(values, signs))
                tempsolution.append(self.format_solution(values, signs))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


    def format_enonce(self, liste, signs):
        powersymbol = "^"
        return self.format_with_power_symbol(liste, signs, powersymbol)

    def format_solution(self, liste, signs):
        powersymbol = "**"
        currentcalc = self.format_with_power_symbol(liste, signs, powersymbol)
        todo = currentcalc.replace("\\times", "*").replace("\\div", "/").replace("$", "").replace("{","(").replace("}",")")
        calcresult = simplify(todo)
        calcresult = str(calcresult).replace("**", "^").replace("*", "\\times ").replace("/", "\\div ").replace("(", "{").replace(")", "}")
        return "$%s$" % (calcresult)


    def format_with_power_symbol(self, liste, signs, powersymbol):
        string = "$"
        puissancesymbol = powersymbol
        i = 0
        while i < len(liste):
            if i!=len(liste)-1:
                string += "%s%s{%s} %s " % (liste[i][0], puissancesymbol, liste[i][1], signs[i])
            else:
                string += "%s%s{%s}" % (liste[i][0], puissancesymbol, liste[i][1])
            i+=1
        string += "$"
        return string

if __name__ == "__main__":
    app = AdditionDecimaux()
    app.display()