__author__ = 'mrmen'

from TemplateExercice import *
import random


class Division(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = 10
        self.max = 500
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                first = random.randint(self.min, self.max)
                second = random.randint(self.min, self.max)
                first, second = max(first, second), min(first, second)
                tempenonce.append("%s \\div %s" % (first, second))
                tempsolution.append("\\shadowbox{\\opdiv[displayshiftintermediary=all,displayintermediary=nonzero,hfactor=decimal]{%s}{%s}}" % (first, second))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = Division()
    app.display()
