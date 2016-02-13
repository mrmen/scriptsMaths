__author__ = 'mrmen'

from TemplateExercice import *
import random
from sympy import abc, simplify


class Developpement(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = -10
        self.max = 10
        self.nb = ["x", "y", ""]
        self.sign = ["\\times"]
        self.generate()

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
                    value = random.randint(self.min, self.max)
                    values.append([value, self.nb[random.randint(0,len(self.nb)-1)])
                #
                tempenonce.append(self.format_enonce(values))
                tempsolution.append(self.format_solution(values))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


    def format_enonce(self, liste):
        string = []
        for elt in liste:
            fact = elt[0]
            variable = elt[1]
            if variable == "":
                variable = 1              
            string.append(str(fact) + "\\times" + str(variable))
         return self.concat_enonce(string)

    def concat_enonce(liste):
        count = 0
        string = "("
        for _ in liste:
            string += _
            count +=1
            if count == 2:
                string+=")("
        string+=")"
        return "$" + string + "$"

    def format_solution(self, liste):
        return "None"

if __name__ == "__main__":
    app = AdditionDecimaux()
    app.display()
